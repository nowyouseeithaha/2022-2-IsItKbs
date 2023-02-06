import os
import pickle
import pandas as pd

def train_and_save_model(clf_class, features_file, target_file, model_file):
    os_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    
    with open (os_path + "/data/processed/" + features_file, "rb") as f1:
        X = pickle.load(f1)
    
    with open (os_path + "/data/processed/" + target_file, "rb") as f2:
        Y = pd.read_csv(f2, keep_default_na=False).squeeze(1)
    
    model = clf_class()
    model.fit(X, Y)
    
    with open (os_path + "/models/" + model_file, "wb") as f4:
        pickle.dump(model, f4)