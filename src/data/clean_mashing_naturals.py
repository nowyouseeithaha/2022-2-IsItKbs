import pandas as pd
import string

def removevazio(lista):
    for i in range(len(lista)):
     lista[i] = lista[i].strip()

with open(".\\data\\raw\\mashing.txt", "r", encoding="utf-8") as g:
    mashings = g.read()

mashings = mashings.split("\n")

#Remoção dos espaços vazios
removevazio(mashings)

with open(".\\data\\raw\\large-2014.txt", "r", encoding="utf-8") as k:
    naturals = k.read()

naturals = naturals.split(" ")

#Remoção dos espaços vazios
removevazio(naturals)

#Função para remoção de valores númericos e de pontuação das palavras "comuns" da base de dados      
naturals = list(filter(lambda token: token not in string.punctuation and token.isalpha(), naturals))

#Definição de duas séries de dados, uma com as palavras que são mashing e outra com as palavras naturais.
#Logo após ambas são exportadas como .csv
X0 = pd.Series(naturals)
X1 = pd.Series(mashings)
X0.to_csv(".\\data\\interim\\naturals.csv", index = False)
X1.to_csv(".\\data\\interim\\mashings.csv", index = False)