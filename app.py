import streamlit as st

# Set the title of the app
st.title('House Price Prediction App')

# Sidebar for navigation
def sidebar():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to', ['Prediction', 'Analytics', 'About'])
    return selection

selection = sidebar()

# Prediction Page
if selection == 'Prediction':
    st.header('House Price Prediction')
    sqft = st.number_input('Enter square footage:')
    bedrooms = st.number_input('Enter number of bedrooms:')
    bathrooms = st.number_input('Enter number of bathrooms:')
    if st.button('Predict'):  
        # Replace with model prediction logic
        predicted_price = sqft * 100 + bedrooms * 10000 + bathrooms * 5000  # Example computation
        st.subheader(f'Predicted Price: ${predicted_price}')

# Analytics Page
elif selection == 'Analytics':
    st.header('Analytics')
    st.write('Display analytics and insights about the housing market here.')
    # Add visualization or data analysis logic here.
 
# About Page
elif selection == 'About':
    st.header('About this App')
    st.write('This application uses machine learning to predict house prices based on various parameters.')
    st.write('Created by GameReal00')
