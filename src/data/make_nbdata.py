import pandas as pd
from sklearn.utils import shuffle
from auxiliary import open_csv_df, apply_lexicals_ftr, df_concat_reset

X0 = open_csv_df("\\data\\interim\\naturals.csv")
X1 = open_csv_df("\\data\\interim\\mashings.csv")

X0 = shuffle(X0, random_state=777).reset_index(drop=True)

X0["mash"] = 0
X1["mash"] = 1

df = df_concat_reset(X0, X1)
df = apply_lexicals_ftr(df)

df.to_csv(".\\data\\processed\\nbdata2.csv", index = False)
df["mash"].to_csv(".\\data\\processed\\nb_targe2t.csv", index = False)