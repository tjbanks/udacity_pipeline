import pandas as pd
from sqlalchemy import create_engine
import sys


def load_data(messages_filepath, categories_filepath):
    """
    Load message and category datasets and return a single pandas
    dataframe.
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    # Merge the messages and categories datasets using the common id
    df = messages.merge(categories, left_on='id',right_on='id')

    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(';', expand=True)

    # select the first row of the categories dataframe
    row = categories.iloc[0].tolist()
    # use this row to extract a list of new column names for categories.
    category_colnames = [i[:-2] for i in row]

    categories.columns = category_colnames

    # - Iterate through the category columns in df to keep only the last 
    # character of each string (the 1 or 0). For example, `related-0` 
    # becomes `0`, `related-1` becomes `1`. Convert the string to a numeric value.
    for column in categories:
        # set each value to be the last character of the string
        categories[column] =  categories[column].map(lambda x: x[-1])
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    # drop the original categories column from `df`
    df.drop(columns=['categories'],inplace=True)

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df,categories],axis=1)

    return df

def clean_data(df):
    """
    Cleans the provided dataframe, removes duplicate values currently.
    """
    df = df[~df.duplicated()]
    return df


def save_data(df, database_filename):
    """
    Saves the provided dataframe to the specified sqlite database file.
    """
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('Messages', engine, index=False)  


def main():
    if len(sys.argv) == 4:
        #eg: data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()