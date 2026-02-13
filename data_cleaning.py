import pandas as pd
import numpy as np

# Load the dataset

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Handle missing values

def handle_missing_values(data):
    # Example: Fill missing numeric values with the mean
    for column in data.select_dtypes(include=[np.number]).columns:
        data[column].fillna(data[column].mean(), inplace=True)
    # Example: Drop rows with missing categorical values
    data.dropna(subset=['some_categorical_column'], inplace=True)
    return data

# Remove outliers

def remove_outliers(data):
    # Example: Remove outliers using the IQR method
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
    return data

# Standardize data types

def standardize_data_types(data):
    # Example: Ensure 'date' columns are of datetime type
    data['date_column'] = pd.to_datetime(data['date_column'], errors='coerce')
    return data

# Remove duplicates

def remove_duplicates(data):
    data.drop_duplicates(inplace=True)
    return data

# Full data cleaning process

def clean_data(file_path):
    data = load_data(file_path)
    data = handle_missing_values(data)
    data = remove_outliers(data)
    data = standardize_data_types(data)
    data = remove_duplicates(data)
    return data

# Example usage
if __name__ == '__main__':
    cleaned_data = clean_data('nigeria_houses_data.csv')
    cleaned_data.to_csv('cleaned_nigeria_houses_data.csv', index=False)