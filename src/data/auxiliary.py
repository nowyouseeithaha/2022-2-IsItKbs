import os
import pandas as pd

def letter_counter(string, type=None):
    if (type == 'c'):
        return {letter: str(string).count(letter) for letter in 'bcdfghjklmnpqrstvwxyz'}
    elif (type == 'v'):
        return {letter: str(string).count(letter) for letter in 'aeiou'}  
    return {letter: str(string).count(letter) for letter in 'abcdefghijklmnopqrstuvwxyz'}

def type_counter(string, type=None):    
    return sum(letter_counter(string, type).values())
    
def type_ratio(string, type=None):
    if (len(string) == 0):
        return 0
    return type_counter(string, type)/len(string)

def ttr(string):
    if (len(string) == 0):
        return 0
    ttr = len(set(string)) / len(string)
    return ttr

def open_csv_df(filepath):
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) + filepath
    with open (path, "r", encoding="utf-8") as file0:
        rtn = pd.DataFrame(pd.read_csv(file0, keep_default_na=False))
    return rtn

def apply_lexicals_ftr(df):
    df["vowel rt"] = df["words"].apply(lambda x : type_ratio(str(x), 'v'))
    df["consonant rt"] = df["vowel rt"].apply(lambda x : 1-x)
    df["ttr"] = df["words"].apply(ttr)

    return df

def df_concat_reset(df1, df2):
    return pd.concat([df1, df2], axis=0).rename(columns={'0':'words'}, inplace=False).reset_index(drop=True)
