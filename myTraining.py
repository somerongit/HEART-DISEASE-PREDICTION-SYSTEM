import numpy as np
import pandas as pd
from sklearn.svm import SVC
import pickle


if __name__ == "__main__":
    df = pd.read_csv('heart.csv')
    x_val = df.iloc[0:,0:len(df.columns)-1].values
    y_val = df.iloc[0:,-1].values
    clf =  SVC(kernel='rbf', C=2)
    clf.fit(x_val, y_val)
    file = open('model.pkl', 'wb')
    pickle.dump(clf, file)
    file.close()