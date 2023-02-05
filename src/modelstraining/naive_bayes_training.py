from sklearn.naive_bayes import MultinomialNB
from train_save_clf import train_and_save_model

train_and_save_model(MultinomialNB, "nb_vectfeatures.pkl", "nb_target.csv", "naivebayes.pkl")