# -*- coding: utf-8 -*-
"""MLu_RndForestIII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i7oNgBvdXVuu_KEVwbySHFZod3SzinuB
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

#Base de dados censo americano
base_census = pd.read_csv('/content/census.csv')

base_census
#discreta:age, final weight, education num, capital ganho, capital perda, hora semanal, income
#ordinal: education
#nominal: estado cívil, ocupação, relacionamento, raça, sexo, native country

base_census.describe()

base_census.isnull().sum()
#sem nenhum valor negativo ou faltante

np.unique(base_census['income'], return_counts=True)

sns.countplot(x = base_census['income'])

plt.hist(x = base_census['age'])

plt.hist(x = base_census['education-num'])

plt.hist(x= base_census['hour-per-week'])

grafico = px.treemap(base_census, path=['occupation'])
grafico.show()

grafico = px.parallel_categories(base_census, dimensions=['occupation', 'relationship'])
grafico.show()

X_census = base_census.iloc[:, 0:14].values

X_census

Y_census = base_census.iloc[:, 14].values

Y_census

#Tratamento de atributos categóricos
#labelEncoder
from sklearn.preprocessing import LabelEncoder

label_encoder_teste =  LabelEncoder()
teste = label_encoder_teste.fit_transform(X_census[:, 1])

X_census[:, 1]

teste

X_census[0]

label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

X_census[:, 1] = label_encoder_workclass.fit_transform(X_census[:,1])
X_census[:, 3] = label_encoder_education.fit_transform(X_census[:,3])
X_census[:, 5] = label_encoder_marital.fit_transform(X_census[:,5])
X_census[:, 6] = label_encoder_occupation.fit_transform(X_census[:,6])
X_census[:, 7] = label_encoder_relationship.fit_transform(X_census[:,7])
X_census[:, 8] = label_encoder_race.fit_transform(X_census[:,8])
X_census[:, 9] = label_encoder_sex.fit_transform(X_census[:,9])
X_census[:, 13] = label_encoder_country.fit_transform(X_census[:,13])

X_census

#OneHotEncoder
#transforma uma coluna ex "carro" palio, gol, uno em três colunas. Ao invés de serem calssificados como 1, 2 e 3 é classifcado como
#palio 1 0 0
#uno 0 1 0
#gol 0 0 1
#evitando o algoritmo atribuir um peso maior em decorrência do valor mais alto

len(np.unique(base_census['occupation']))

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

onehotencoder_census = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])],remainder="passthrough")

X_census = onehotencoder_census.fit_transform(X_census).toarray()

X_census[0]

X_census.shape
#de 15 colunas para 108

#Escalonamento dos valores
from sklearn.preprocessing import StandardScaler
scaler_census = StandardScaler()
X_census = scaler_census.fit_transform(X_census)

X_census[0]

from sklearn.model_selection import train_test_split
#divisão treino e teste
X_census_treinamento, X_census_teste, Y_census_treinamento, Y_census_teste = train_test_split(X_census, Y_census, test_size = 0.25, random_state = 0)

X_census_teste.shape, Y_census_teste.shape

X_census_treinamento.shape, Y_census_treinamento.shape

import pickle
with open('census.pkl', mode = 'wb' ) as f:
  pickle.dump([X_census_treinamento, Y_census_treinamento, X_census_teste, Y_census_teste], f)

from sklearn.ensemble import RandomForestClassifier
random_forest_census = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
random_forest_census.fit(X_census_treinamento, Y_census_treinamento)

previsoes = random_forest_census.predict(X_census_teste)

previsoes

from sklearn.metrics import accuracy_score, classification_report
accuracy_score(Y_census_teste, previsoes)

from yellowbrick.classifier import ConfusionMatrix
cm = ConfusionMatrix(random_forest_census)
cm.fit(X_census_treinamento, Y_census_treinamento)
cm.score(X_census_teste, Y_census_teste)

print(classification_report(Y_census_teste, previsoes))