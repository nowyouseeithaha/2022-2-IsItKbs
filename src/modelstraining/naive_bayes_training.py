from sklearn.naive_bayes import MultinomialNB #, ComplementNB, BernoulliNB
import pandas as pd
import pickle
import os

os_path = os.path.dirname(os.path.realpath('__file__'))

#Leitura das features
with open (os_path + '/data/processed/ngrams_vectfeatures.pkl', "rb") as f1:
    X = pickle.load(f1)

#Leitura dos targets
with open (os_path + '/data/processed/ngrams_target.csv', "rb") as f2:
    Y = pd.read_csv(f2, keep_default_na=False).squeeze(1)

#Leitura do vetorizador que foi usado nas features
with open (os_path + '/models/tfid_vectorizer.pkl', "rb") as f3:
    vectorizer = pickle.load(f3)

#Instanciação do modelo
model = MultinomialNB()
model.fit(X,Y)

#Compressão do modelo para um pickle
with open (os_path + '/models/naivebayes.pkl', "wb") as f4:
    pickle.dump(model, f4)

f1.close(), f2.close(), f3.close(), f4.close()