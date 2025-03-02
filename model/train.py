import csv
from sklearn import svm
import sklearn
import sklearn.datasets
import sklearn.model_selection

y_hv = []

x_hv = []



y = []

x = []

with open("data.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader, None)
    for i, line in enumerate(reader):
        print(i)
        y_hv.append(line[0])
        x_hv.append(line[1:])

with open("data1.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    next(reader, None)
    for i, line in enumerate(reader):
        print(i)
        y.append(line[0])
        x.append(line[1:])

X_hv_train, X_hv_test, y_hv_train, y_hv_test = sklearn.model_selection.train_test_split(x_hv, y_hv,
                                                    stratify=y_hv, 
                                                    test_size=0.25, random_state=69)
clf_hv = svm.SVC()
clf_hv.fit(X_hv_train, y_hv_train)

clf_hv = svm.SVC()
clf_hv.fit(X_hv_train, y_hv_train)

X_hv_unstr_train, X_hv_unstr_test, y_hv_unstr_train, y_hv_unstr_test = sklearn.model_selection.train_test_split(x_hv, y_hv,
                                                    test_size=0.25, random_state=69)
clf_hv = svm.SVC()
clf_hv.fit(X_hv_train, y_hv_train)

clf = svm.SVC()
clf.fit(X_hv_unstr_train, y_hv_unstr_train)

print("Trained!\n")
print(f"Horizontal/vertical stratified: {clf_hv.score(X_hv_test, y_hv_test)}")
print(f"Horizontal/vertical unstratified: {clf.score(X_hv_unstr_test, y_hv_unstr_test)}")

import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(clf_hv, f)
