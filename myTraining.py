import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
def data_split(heart, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(heart))
    test_set_size = int(len(heart) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return heart.iloc[train_indices], heart.iloc[test_indices]


if __name__ == "__main__":
    df = pd.read_csv('heart.csv')
    train, test = data_split(df, 0.3)
    X_train = train[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']].to_numpy()
    X_test = test[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']].to_numpy()
    Y_train = train[['target']].to_numpy().reshape(229 ,)
    Y_test = test[['target']].to_numpy().reshape(97 ,)
    clf = LogisticRegression(solver='liblinear')
    clf.fit(X_train, Y_train)
    file = open('model.pkl', 'wb')
    pickle.dump(clf, file)
    file.close()