# -*- coding: utf-8 -*-
"""Utilzando algoritimos de classificação para determinar se um nome é masculino ou feminino baseado nas letras iniciais, finais e quantidade de letras

Original file is located at
    https://colab.research.google.com/drive/1sZDIJmfcOn80yvzn3LF8EdUUtgrPHsCW
"""

import nltk
nltk.download('names')

from nltk. corpus import names
import random
nomes_masculinos = [(nome,'masc') for nome in names.words("male.txt")]
nomes_femininos = [(nome,'fem') for nome in names.words("female.txt")]

nomes = nomes_masculinos + nomes_femininos
random.shuffle(nomes)

for nome in nomes[:10]:
  print(nome)

"""extrair feature primeira letra, ultima letra e quantidade de caracteres"""
print("Nome:",nomes[0][0])
print("Primeira letra:",nomes[0][0][0].lower())
print("ùltima letra:",nomes[0][0][-1].lower())
print("Quantidade:", len(nomes[0][0]))

#convertendo caracteres por números
caracter_to_int = {c:i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz_')}
try:
  print(caracter_to_int['k'])
except:
  print(caracter_to_int['_'])

def extrair_features(nome):
  caracter_to_int = {c:i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz_')}

  try:
      primeiro_caractere = caracter_to_int[nome.lower()[0]]

  except:
    print(caracter_to_int['_'])

  try:
      ultimo_caractere = caracter_to_int[nome.lower()[-1]]

  except:
    print(caracter_to_int['_'])


  total_caractere = len(nome)

  return(primeiro_caractere, ultimo_caractere, total_caractere)

extrair_features(nomes[0][0])

X, y = [], []
for row in nomes[:10]:
  nome, categoria = row
  features = extrair_features(nome)
  classe = 1 if categoria =='fem' else 0

  X.append(features)
  y.append(classe)

from sklearn.tree import DecisionTreeClassifier

ad = DecisionTreeClassifier()
ad = ad.fit(X,y)

    
nome = 'Felipe'
feature = extrair_features(nome)
rad = ad.predict([feature])
if rad == 1:
    print(nome, " Feminino")
else:
    print(nome, " Masculino")
    
from sklearn.naive_bayes import GaussianNB

nb = DecisionTreeClassifier()
nb.fit(X,y)

nome = 'Felipe'
feature = extrair_features(nome)
rnb = nb.predict([feature])

if rnb == 1:
    print(nome, " Feminino")
else:
    print(nome, " Masculino")
    