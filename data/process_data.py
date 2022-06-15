import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    Load the two datasets and merge them
    Args:
        -messages_filepath (csv) : Message Dataset path
        -categories_filepath (csv) : Categories Dataset path
    Returns:
        -df (DataFrame): Dataframe containing the merge of the message and categories csvs
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    return df


def clean_data(df):
    """
    Clean the dataframe returning in output the message and the one-hot encoding of the corrisponding values
    Args:
        -df (DataFrame): Dataframe containing the merge of the message and categories csvs
    Returns:
        -df (DataFrame): Dataframe containing the message and the one-hot encoding of the values
       
    """
    categories = df["categories"].str.split(";", expand = True)
    # select the first row of the categories dataframe
    row = categories[:1]

    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = row.apply(lambda x : x.values[0][0:-2])
    # rename the columns of `categories`
    categories.columns = category_colnames
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str.slice(-1)
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    df = df.drop(['categories'], axis=1)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
    df = df.drop_duplicates()
    return df


def save_data(df, database_filename):
    """
    Save the dataframe in the provided filepath in a DB format
        -df (dataframe) : DF which needs to be saved
        -database_filename (str): Path where to save the df
    Returns:
    """
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('disaster_msg_tbl', engine, index=False)  


def main():
    """
    Main function
    """
    if len(sys.argv) == 4:

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