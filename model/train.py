import csv
from sklearn import svm
import sklearn
import sklearn.datasets
import sklearn.model_selection

y_hv = []
x_hv = []

with open("data.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader, None)
    for i, line in enumerate(reader):
        print(i)
        y_hv.append(line[0])
        x_hv.append(line[1:])

X_hv_train, X_hv_test, y_hv_train, y_hv_test = sklearn.model_selection.train_test_split(x_hv, y_hv,
                                                    stratify=y_hv, 
                                                    test_size=0.25, random_state=69)

clf_hv = svm.SVC()
clf_hv.fit(X_hv_train, y_hv_train)

print("Trained!\n")
print(f"Horizontal/vertical stratified: {clf_hv.score(X_hv_test, y_hv_test)}")

import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(clf_hv, f)
