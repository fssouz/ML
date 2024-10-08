# -*- coding: utf-8 -*-
"""MLU_Tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WkeLwsBrMekvjH7dVD-mrnV0WA06fpMm
"""

from sklearn.tree import DecisionTreeClassifier

import pickle
with open('risco_credito.pkl', 'rb') as f:
  X_risco_credito, y_risco_credito = pickle.load(f)

y_risco_credito

arvore_risco_credito = DecisionTreeClassifier(criterion="entropy")
arvore_risco_credito.fit(X_risco_credito, y_risco_credito)

arvore_risco_credito.feature_importances_

from sklearn import tree
previsores = ['historia', 'dívida', 'garantias', 'renda']
tree.plot_tree(arvore_risco_credito, feature_names=previsores, class_names=arvore_risco_credito.classes_);

#historia boa, dívida alta, garantias nenhuma, renda >35
#historia ruim, divida alta, garantias adequadas, renda <15
previsoes = arvore_risco_credito.predict([[0,0,1,2],[2,0,0,0]])
previsoes