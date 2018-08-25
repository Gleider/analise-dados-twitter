import csv
import re
import nltk
import string
import unicodedata
import sys



# reload(sys)
# sys.setdefaultencoding("utf-8")

def ler_arquivo():
  with open('amostra.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for linha in reader:
      print(remove_stopwords(linha[2]))

def remove_stopwords(tweet):
  palavras = []
  p = tweet.split()
  for t in p:
    if t not in palavras:
      palavras.append(t)
  stopwords = nltk.corpus.stopwords.words('portuguese')
  conteudo = [w for w in palavras if w.lower().strip() not in stopwords]
  return conteudo

ler_arquivo()