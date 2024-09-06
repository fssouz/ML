# -*- coding: utf-8 -*-
"""MLU_knnCredit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aDfJ7i2QzEoDJ63zevB5Zf2OIjyc_7sH
"""

from sklearn.neighbors import KNeighborsClassifier
import pickle
with open('credit.pkl', 'rb') as f:
  X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)

#dataset já normalizado
X_credit_treinamento

X_credit_treinamento.shape

knn_credit = KNeighborsClassifier(n_neighbors=5, metric='minkowski')

knn_credit.fit(X_credit_treinamento, y_credit_treinamento)

previsoes = knn_credit.predict(X_credit_teste)
previsoes

from sklearn.metrics import accuracy_score, classification_report

accuracy_score(y_credit_teste, previsoes)

from yellowbrick.classifier import ConfusionMatrix
cm = ConfusionMatrix(knn_credit)
cm.fit(X_credit_treinamento, y_credit_treinamento)
cm.score(X_credit_teste, y_credit_teste)

print(classification_report(y_credit_teste, previsoes))