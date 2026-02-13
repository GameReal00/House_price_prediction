import pandas as pd  
import numpy as np  
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler, KBinsDiscretizer
from sklearn.compose import ColumnTransformer  
from sklearn.pipeline import Pipeline

# Load dataset  
def load_data(filepath):  
    return pd.read_csv(filepath)

# Numerical feature engineering  
def numerical_features(df):  
    num_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()  
    # Example transformations  
    df['log_area'] = np.log(df['area'])  
    df['price_per_sqft'] = df['price'] / df['area']  
    return df[num_features + ['log_area', 'price_per_sqft']]

# Categorical feature engineering  
def categorical_features(df):  
    cat_features = df.select_dtypes(include=['object']).columns.tolist()  
    encoder = OneHotEncoder(drop='first', sparse=False)
    encoded_features = encoder.fit_transform(df[cat_features])
    return pd.DataFrame(encoded_features, columns=encoder.get_feature_names(cat_features))

# Interaction features  
def interaction_features(df):  
    df['area_beds'] = df['area'] * df['bedrooms']  
    df['bath_to_bed_ratio'] = df['bathrooms'] / df['bedrooms']  
    return df[['area_beds', 'bath_to_bed_ratio']]

# Statistical features  
def statistical_features(df):  
    df['mean_price'] = df['price'].mean()  
    df['median_sqft'] = df['price'] / df['area']  
    return df[['mean_price', 'median_sqft']]

# Polynomial features  
def polynomial_feature_engineering(df):  
    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly_features = poly.fit_transform(df[['area', 'bedrooms', 'bathrooms']])
    return pd.DataFrame(poly_features, columns=poly.get_feature_names(['area', 'bedrooms', 'bathrooms']))

# Binning features  
def binning_features(df):  
    binning = KBinsDiscretizer(n_bins=3, encode='onehot-dense', strategy='uniform')
    binned_data = binning.fit_transform(df[['price']])
    return pd.DataFrame(binned_data, columns=['price_low', 'price_mid', 'price_high'])

# Complete feature engineering function  
def feature_engineering(filepath):  
    df = load_data(filepath)  
    df = df.join(numerical_features(df))  
    df = df.join(categorical_features(df))  
    df = df.join(interaction_features(df))  
    df = df.join(statistical_features(df))  
    df = df.join(polynomial_feature_engineering(df))  
    df = df.join(binning_features(df))  
    return df