import pandas as pd
from nltk import everygrams
from sklearn.utils import shuffle
import numpy as np

with open (".\\data\\interim\\naturals.csv", "r", encoding="utf-8") as file0:
    X0 = pd.DataFrame(pd.read_csv(file0, keep_default_na=False))

with open (".\\data\\interim\\mashings.csv", "r", encoding="utf-8") as file1:
    X1 = pd.DataFrame(pd.read_csv(file1, keep_default_na=False))

X0 = shuffle(X0, random_state=777).reset_index(drop=True)
X0 = X0[:len(X1)]

X0["mash"] = 0
X1["mash"] = 1
df = pd.concat([X0, X1], axis=0).rename(columns={'0':'words'}, inplace=False).reset_index(drop=True)
df.to_csv(".\\data\\processed\\rfdata.csv", index = False)