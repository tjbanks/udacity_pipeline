# Disaster Response Pipeline Project

## Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


## Example Use

### process_data.py
```
> python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
Loading data...
    MESSAGES: data/disaster_messages.csv
    CATEGORIES: data/disaster_categories.csv
Cleaning data...
Saving data...
    DATABASE: data/DisasterResponse.db
Cleaned data saved to database!
```

### train_classifier.py
```
> python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
[nltk_data] Downloading package punkt to
[nltk_data]     C:\Users\Tyler\AppData\Roaming\nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\Tyler\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
Loading data...
    DATABASE: data/DisasterResponse.db
Building model...
Training model...
Evaluating model...
related
              precision    recall  f1-score   support

           0       0.73      0.25      0.37      1214
           1       0.80      0.97      0.88      3992
           2       0.50      0.08      0.14        38

    accuracy                           0.80      5244
   macro avg       0.68      0.43      0.46      5244
weighted avg       0.79      0.80      0.76      5244

request
              precision    recall  f1-score   support

           0       0.89      0.99      0.94      4336
           1       0.87      0.41      0.56       908

    accuracy                           0.89      5244
   macro avg       0.88      0.70      0.75      5244
weighted avg       0.89      0.89      0.87      5244

offer
C:\Users\Tyler\anaconda3\lib\site-packages\sklearn\metrics\_classification.py:1272: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5220
           1       0.00      0.00      0.00        24

    accuracy                           1.00      5244
   macro avg       0.50      0.50      0.50      5244
weighted avg       0.99      1.00      0.99      5244

aid_related
              precision    recall  f1-score   support

           0       0.76      0.87      0.81      3113
           1       0.76      0.61      0.67      2131

    accuracy                           0.76      5244
   macro avg       0.76      0.74      0.74      5244
weighted avg       0.76      0.76      0.76      5244

medical_help
              precision    recall  f1-score   support

           0       0.92      1.00      0.96      4824
           1       0.71      0.05      0.09       420

    accuracy                           0.92      5244
   macro avg       0.82      0.52      0.52      5244
weighted avg       0.91      0.92      0.89      5244

medical_products
              precision    recall  f1-score   support

           0       0.95      1.00      0.98      4983
           1       0.70      0.05      0.10       261

    accuracy                           0.95      5244
   macro avg       0.83      0.53      0.54      5244
weighted avg       0.94      0.95      0.93      5244

search_and_rescue
              precision    recall  f1-score   support

           0       0.97      1.00      0.99      5093
           1       0.73      0.05      0.10       151

    accuracy                           0.97      5244
   macro avg       0.85      0.53      0.54      5244
weighted avg       0.97      0.97      0.96      5244

security
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5144
           1       0.33      0.01      0.02       100

    accuracy                           0.98      5244
   macro avg       0.66      0.50      0.50      5244
weighted avg       0.97      0.98      0.97      5244

military
              precision    recall  f1-score   support

           0       0.97      1.00      0.99      5090
           1       0.60      0.04      0.07       154

    accuracy                           0.97      5244
   macro avg       0.79      0.52      0.53      5244
weighted avg       0.96      0.97      0.96      5244

child_alone
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5244

    accuracy                           1.00      5244
   macro avg       1.00      1.00      1.00      5244
weighted avg       1.00      1.00      1.00      5244

water
              precision    recall  f1-score   support

           0       0.95      1.00      0.97      4926
           1       0.92      0.22      0.35       318

    accuracy                           0.95      5244
   macro avg       0.94      0.61      0.66      5244
weighted avg       0.95      0.95      0.94      5244

food
              precision    recall  f1-score   support

           0       0.93      0.99      0.96      4663
           1       0.86      0.38      0.53       581

    accuracy                           0.92      5244
   macro avg       0.89      0.69      0.74      5244
weighted avg       0.92      0.92      0.91      5244

shelter
              precision    recall  f1-score   support

           0       0.93      1.00      0.96      4789
           1       0.85      0.26      0.40       455

    accuracy                           0.93      5244
   macro avg       0.89      0.63      0.68      5244
weighted avg       0.93      0.93      0.91      5244

clothing
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5174
           1       0.60      0.04      0.08        70

    accuracy                           0.99      5244
   macro avg       0.79      0.52      0.54      5244
weighted avg       0.98      0.99      0.98      5244

money
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5132
           1       0.83      0.04      0.08       112

    accuracy                           0.98      5244
   macro avg       0.91      0.52      0.54      5244
weighted avg       0.98      0.98      0.97      5244

missing_people
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5176
           1       0.00      0.00      0.00        68

    accuracy                           0.99      5244
   macro avg       0.49      0.50      0.50      5244
weighted avg       0.97      0.99      0.98      5244

refugees
              precision    recall  f1-score   support

           0       0.97      1.00      0.98      5061
           1       0.25      0.01      0.01       183

    accuracy                           0.96      5244
   macro avg       0.61      0.50      0.50      5244
weighted avg       0.94      0.96      0.95      5244

death
              precision    recall  f1-score   support

           0       0.96      1.00      0.98      5008
           1       0.79      0.08      0.15       236

    accuracy                           0.96      5244
   macro avg       0.88      0.54      0.56      5244
weighted avg       0.95      0.96      0.94      5244

other_aid
              precision    recall  f1-score   support

           0       0.88      1.00      0.93      4584
           1       0.52      0.02      0.03       660

    accuracy                           0.87      5244
   macro avg       0.70      0.51      0.48      5244
weighted avg       0.83      0.87      0.82      5244

infrastructure_related
              precision    recall  f1-score   support

           0       0.94      1.00      0.97      4906
           1       0.00      0.00      0.00       338

    accuracy                           0.93      5244
   macro avg       0.47      0.50      0.48      5244
weighted avg       0.88      0.93      0.90      5244

transport
              precision    recall  f1-score   support

           0       0.96      1.00      0.98      5015
           1       0.60      0.05      0.10       229

    accuracy                           0.96      5244
   macro avg       0.78      0.53      0.54      5244
weighted avg       0.94      0.96      0.94      5244

buildings
              precision    recall  f1-score   support

           0       0.95      1.00      0.97      4963
           1       0.95      0.06      0.12       281

    accuracy                           0.95      5244
   macro avg       0.95      0.53      0.55      5244
weighted avg       0.95      0.95      0.93      5244

electricity
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5145
           1       0.50      0.01      0.02        99

    accuracy                           0.98      5244
   macro avg       0.74      0.50      0.51      5244
weighted avg       0.97      0.98      0.97      5244

tools
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5220
           1       0.00      0.00      0.00        24

    accuracy                           1.00      5244
   macro avg       0.50      0.50      0.50      5244
weighted avg       0.99      1.00      0.99      5244

hospitals
              precision    recall  f1-score   support

           0       0.99      1.00      1.00      5194
           1       0.00      0.00      0.00        50

    accuracy                           0.99      5244
   macro avg       0.50      0.50      0.50      5244
weighted avg       0.98      0.99      0.99      5244

shops
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      5222
           1       0.00      0.00      0.00        22

    accuracy                           1.00      5244
   macro avg       0.50      0.50      0.50      5244
weighted avg       0.99      1.00      0.99      5244

aid_centers
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5184
           1       0.00      0.00      0.00        60

    accuracy                           0.99      5244
   macro avg       0.49      0.50      0.50      5244
weighted avg       0.98      0.99      0.98      5244

other_infrastructure
              precision    recall  f1-score   support

           0       0.96      1.00      0.98      5011
           1       0.00      0.00      0.00       233

    accuracy                           0.95      5244
   macro avg       0.48      0.50      0.49      5244
weighted avg       0.91      0.95      0.93      5244

weather_related
              precision    recall  f1-score   support

           0       0.88      0.97      0.92      3799
           1       0.87      0.64      0.74      1445

    accuracy                           0.88      5244
   macro avg       0.88      0.80      0.83      5244
weighted avg       0.88      0.88      0.87      5244

floods
              precision    recall  f1-score   support

           0       0.95      1.00      0.97      4806
           1       0.92      0.38      0.54       438

    accuracy                           0.95      5244
   macro avg       0.93      0.69      0.75      5244
weighted avg       0.94      0.95      0.93      5244

storm
              precision    recall  f1-score   support

           0       0.94      0.99      0.96      4760
           1       0.76      0.41      0.53       484

    accuracy                           0.93      5244
   macro avg       0.85      0.70      0.75      5244
weighted avg       0.93      0.93      0.92      5244

fire
              precision    recall  f1-score   support

           0       0.99      1.00      0.99      5188
           1       0.00      0.00      0.00        56

    accuracy                           0.99      5244
   macro avg       0.49      0.50      0.50      5244
weighted avg       0.98      0.99      0.98      5244

earthquake
              precision    recall  f1-score   support

           0       0.97      0.99      0.98      4734
           1       0.89      0.76      0.82       510

    accuracy                           0.97      5244
   macro avg       0.93      0.88      0.90      5244
weighted avg       0.97      0.97      0.97      5244

cold
              precision    recall  f1-score   support

           0       0.98      1.00      0.99      5146
           1       0.82      0.09      0.17        98

    accuracy                           0.98      5244
   macro avg       0.90      0.55      0.58      5244
weighted avg       0.98      0.98      0.98      5244

other_weather
              precision    recall  f1-score   support

           0       0.95      1.00      0.97      4983
           1       0.50      0.01      0.02       261

    accuracy                           0.95      5244
   macro avg       0.73      0.50      0.49      5244
weighted avg       0.93      0.95      0.93      5244

direct_report
              precision    recall  f1-score   support

           0       0.87      0.98      0.92      4231
           1       0.85      0.36      0.50      1013

    accuracy                           0.86      5244
   macro avg       0.86      0.67      0.71      5244
weighted avg       0.86      0.86      0.84      5244

Saving model...
    MODEL: models/classifier.pkl
Trained model saved!

```

### run.py

```
> cd app
> python run.py
 * Serving Flask app "run" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with windowsapi reloader
 * Debugger is active!
 * Debugger PIN: 206-701-020
 * Running on http://0.0.0.0:3001/ (Press CTRL+C to quit)
```