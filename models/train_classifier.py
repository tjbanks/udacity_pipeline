import nltk
nltk.download(['punkt', 'wordnet'])

import re
import numpy as np
import pandas as pd
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sqlalchemy import create_engine
import sys

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


def load_data(database_filepath):
    """
    Load the specified database file, return the split, X,Y values
    Along with category names
    """

    engine = create_engine('sqlite:///'+database_filepath)
    df = pd.read_sql_table('Messages', engine) 
    category_names = df.columns[-36:]
    X = df['message']
    Y = df[category_names]

    return X,Y,category_names


def tokenize(text):
    """
    Tokenize the string of text provided
    Replaces URLS
    Lemmatizes and returns the tokens
    """
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """
    Builds a simple pipeline containing:
        CountVectorizer,
        TfidfTransformer
        RandomForestClassifier
    """
    pipeline = Pipeline([
        ('vect',CountVectorizer(tokenizer=tokenize)),
        ('tfidf',TfidfTransformer()),
        ('clf',MultiOutputClassifier(RandomForestClassifier())),
    ])
    return pipeline


def test_other_models(pipeline, X_test, Y_test, category_names):
    """
    Used for testing, proof of thoughts
    """

    parameters = {
        'clf__estimator__n_estimators': [50, 100]
    } # Demonstration of grid search - takes a long time

    cv = GridSearchCV(pipeline, param_grid=parameters)
    cv.fit(X_train,y_train)
    evaluate_model(cv,X_test,Y_test,category_names)

    #
    #pipeline1 = Pipeline([
    #    ('vect',CountVectorizer(tokenizer=tokenize)),
    #    ('tfidf',TfidfTransformer()),
    #    ('clf',MultiOutputClassifier(KNeighborsClassifier())),
    #])
    #pipeline.fit(X_train,y_train)
    #y_pred = pipeline.predict(X_test)
    #print_report(y_test,y_pred)
    #



def evaluate_model(model, X_test, Y_test, category_names):
    """
    Evaluates the performance of the specified model.
    Reports the f1 score, precision and recall for each output category of the dataset.
    """
    y_pred = model.predict(X_test)

    for i in range(36):
        print(category_names[i])
        print(classification_report(np.array(Y_test)[:,i], y_pred[:,i]))#, labels=[df.columns[-36+i]]))


def save_model(model, model_filepath):
    """
    Save the scikitlearn model to a provided pickle file location
    """
    # Dump the trained classifier with Pickle
    # Open the file to save as pkl file
    model_pkl = open(model_filepath, 'wb')
    pickle.dump(model, model_pkl)
    # Close the pickle instances
    model_pkl.close()


def main():
    """
    Main entry point
    """
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()