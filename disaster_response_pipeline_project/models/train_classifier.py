import sys
from sqlalchemy import create_engine

import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger', 'stopwords'])

import re
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import pickle
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report, accuracy_score

from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression


def load_data(database_filepath):
    """
    Load the database from the provided filepath
    Args:
        -database_filepath (str) : The path where to find the database
    Returns:
        -X (list) : List of all the messages
        -Y (list): List of the values in the corresponding categories
        -category_names (list): List of all the category names
    """
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('disaster_msg_tbl', engine)  
    X = df.message
    Y = df.drop(columns=["id", "message", "original", "genre"])
    category_names = list(df.columns[4:])
    return X, Y, category_names


def tokenize(text):
    """
    Given a text, return the tokenized version of it.
    Args:
        -text (str) : Text that need to be tokenized
    Returns:
        -clean_tokens(list): List of the tokens coming from the tokenization process
    """
    # Normalize
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]", " ", text)
    # Tokenize
    token = word_tokenize(text)
    # Remove stop words
    filtered_words = [word for word in token if word not in stopwords.words('english')]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(word) for word in filtered_words]
    return clean_tokens


def build_model():
    """
    Build the model which will be used for the prediction.
    Args:
    Returns:
        -cv (model): Model which need to be trained
    """
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])

    parameters = {
        'clf__estimator__n_estimators': [50, 100, 200],
        'clf__estimator__min_samples_split': [2, 3, 4]
    }

    cv = GridSearchCV(pipeline, param_grid=parameters)

    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    """
    Evaluate the model and return the accuracy
    Args:
        -model (model) : Model which needs to be evaluated
        -X_test (list): Data that needs to be tested
        -Y_test (list): Ground truth of the test data
        -category_names (list): Name of all the categories in the df
    Returns:
    """
    y_pred = model.predict(X_test)
    accuracy = (y_pred == Y_test.values).mean()
    print(classification_report(Y_test.iloc[:, 1:].values, np.array([x[1:] for x in y_pred])))#, target_names = category_names))
    print('The model accuracy is {:.3f}'.format(accuracy))


def save_model(model, model_filepath):
    """
    Save the model in the provided filepath
        -model (model) : Model which needs to be saved
        -model_filepath (str): Path where to save the model
    Returns:
    """
    with open (model_filepath, 'wb') as f:
        pickle.dump(model, f)  


def main():
    """
    Main fuction
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
