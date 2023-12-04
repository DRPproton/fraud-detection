import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# st.set_option('server.maxUploadSize', 1000)

st.set_page_config(page_title="Ask your CSV")
st.header("Carga tu CSV 📈")

csv_file = st.file_uploader("Upload a CSV file", type="csv")

if csv_file is not None:
    df = pd.read_csv(csv_file)

    st.dataframe(df)

    option = st.selectbox(label='Eligé un modelo de prediciôn',
                          options=('', '2013', '2023'))
    if option=='':
        st.write('Favor elige una opcion')
    else:
        if option == '2013':
            # Load from file
            try:
                with open("rfc_model.pkl", 'rb') as file:
                    pickle_model = pickle.load(file)
                st.success('Model loaded.')
            except:
                st.write('Error, trata una vez mas')

        else:
            try:
                with open("rfc_model_23.pkl", 'rb') as file:
                    pickle_model = pickle.load(file)
                st.success('Model loaded.')
            except:
                st.write('Error, trata una vez mas')

        cols_for_models_13 = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                              'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
                              'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount', 'Hour']
        cols_for_models_23 = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
                              'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
                              'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

        if pickle_model and option == '2013':
            df["Hour"] = df["Time"].apply(lambda x: np.ceil(float(x) / 3600) % 24)
            df["Hour"] = df["Hour"].astype("int")

            X = df.loc[:, cols_for_models_13]
            y = df.Class

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

            cm = confusion_matrix(y_test, pickle_model.predict(X_test))

            st.dataframe(cm)
            # st.write(f"<p style = 'text-align: center;'> Prediciones Verdaderas Positivas {cm[1][1]}</p>", unsafe_allow_html=True)
            st.write(f'Prediciones Verdaderas Positivas = {cm[1][1]}', unsafe_allow_html=True)
            st.write(f'Prediciones Verdaderas Negativas = {cm[0][0]}')
            st.write(f'Prediciones Falsas Positivas = {cm[0][1]}')
            st.write(f'Prediciones Falsas Negativas = {cm[1][0]}')

        elif pickle_model and option == '2023':
            X = df.loc[:, cols_for_models_23]
            y = df.Class

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

            cm = confusion_matrix(y_test, pickle_model.predict(X_test))

            st.dataframe(cm)
        else:
            st.write('Necesita el modelo para el fichero')
