from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import pickle
from train_save_clf import train_and_save_model

train_and_save_model(RandomForestClassifier, "rf_vectfeatures.pkl", "rf_target.csv", "randomforest.pkl")
