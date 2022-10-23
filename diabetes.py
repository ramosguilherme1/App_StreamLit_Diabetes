#IMPORTANDO BIBLIOTECAS
import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#TITULO
st.write("""
Prevendo Diabetes\n
App que utiliza machine learning para prever possível diabetes dos pacientes.\n
Fonte: PIMA - INDIA (Kaggle)
""")

#DATASET
df = pd.read_csv("diabetes.csv")

#CABEÇALHO
st.subheader('Informações dos dados')

#NOME DO USUÁRIO
user_input = st.sidebar.text_input('Digite seu nome')

st.write('Paciente: ', user_input)

#DADOS DE ENTRADA
X = df.drop(['Outcome'],1)
Y = df['Outcome']

#SEPARA TREINO E TESTE - DF
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.2, random_state=42)

#FUNÇÃO COM DADOS DE USUÁRIOS
def get_user_data():
    pregnancies = st.sidebar.slider('Gravidez', 0, 15, 1)
    glucose = st.sidebar.slider('Glicose', 0, 200, 110)
    blood_pressure = st.sidebar.slider('Pressão Sanguinea', 0, 122, 72)
    skin_thickness = st.sidebar.slider('Espessura da pele', 0, 99, 20)
    insulin = st.sidebar.slider('Insulina', 0, 900, 30)
    bmi = st.sidebar.slider('Indice de massa corporal', 0.0, 70.0, 15.0)
    dpf = st.sidebar.slider('Historico familiar de diabetes', 0.0 , 3.0, 0.0)
    age = st.sidebar.slider('Idade', 15, 100, 21)

    user_data = {'gravidez': pregnancies,
                 'Glicose': glucose,
                 'Pressão sanguinea': blood_pressure,
                 'Espessura da pele': skin_thickness,
                 'Insulina': insulin,
                 'Indice_massa_corporal': bmi,
                 'Historico_familiar de diabetes': dpf,
                 'Idade': age
                 }
    features = pd.DataFrame(user_data, index=[0])

    return features

user_input_variables = get_user_data()

#GRAFICO
graf = st.bar_chart(user_input_variables)

st.subheader('Dados do usuário')
st.write(user_input_variables)

dtc = DecisionTreeClassifier(criterion='entropy', max_depth=3)
dtc.fit(X_train, y_train)

#ACC
st.subheader('Acurácia do modelo')
st.write(accuracy_score(y_test, dtc.predict(X_test)) * 100)

#PREDICTION
prediction = dtc.predict(user_input_variables)

st.subheader('Previsaõ: ')
st.write(prediction)
