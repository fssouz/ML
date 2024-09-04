# -*- coding: utf-8 -*-
"""MLU_TreeII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mrXwZNN28gH93b9DHboy8VEVtwllxcPx
"""

from sklearn.tree import DecisionTreeClassifier
import pickle
with open('credit.pkl', 'rb') as f:
  X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste = pickle.load(f)

X_credit_treinamento.shape

arvore_credit = DecisionTreeClassifier(criterion='entropy', random_state=0)

arvore_credit.fit(X_credit_treinamento, y_credit_treinamento)

previsoes = arvore_credit.predict(X_credit_teste)
previsoes

from sklearn.metrics import accuracy_score, classification_report

accuracy_score(y_credit_teste, previsoes)

from yellowbrick.classifier import ConfusionMatrix
cm = ConfusionMatrix(arvore_credit)
cm.fit(X_credit_treinamento, y_credit_treinamento)
cm.score(X_credit_teste, y_credit_teste)

print(classification_report(y_credit_teste, previsoes))

from sklearn import tree
import matplotlib.pyplot as plt
previsores = ['income', 'age', 'loan']
fig, axes = plt.subplots(nrows =1, ncols= 1, figsize = (20,20))
tree.plot_tree(arvore_credit, feature_names=previsores, class_names=['0', '1']);
fig.savefig('arvore_credit.png')