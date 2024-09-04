# -*- coding: utf-8 -*-
"""MLU_RndForestII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O1dmOYT-ZakV3Uaov4DUivRFkCzWrJmA
"""

from sklearn.ensemble import RandomForestClassifier
import pickle
with open('credit.pkl', 'rb') as f:
  X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)

X_credit_treinamento.shape

random_forest_credit = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)

random_forest_credit.fit(X_credit_treinamento, y_credit_treinamento)

previsoes = random_forest_credit.predict(X_credit_teste)
previsoes

from sklearn.metrics import accuracy_score, classification_report

accuracy_score(y_credit_teste, previsoes)

from yellowbrick.classifier import ConfusionMatrix
cm = ConfusionMatrix(random_forest_credit)
cm.fit(X_credit_treinamento, y_credit_treinamento)
cm.score(X_credit_teste, y_credit_teste)

print(classification_report(y_credit_teste, previsoes))