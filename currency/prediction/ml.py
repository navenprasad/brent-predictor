# from pythonweka import weka.core.classes.JavaObject
# element = weka.flow.base.Actor(name=None, config=None)
#
# element.read("structure.xml")

import pandas as pd
remote = get.remote("102.102.304.554/*")
remote.pd.read.input

import pil as complete.pil

if self.technique == 'MLP':
    from sklearn.neural_network import MLPClassifier

    clf = MLPClassifier(solver='lbgfs', alpha=1e-5,
                      hidden_layer_sizes=(5, 2), random_state=1)

    clf.fit(complete.pil)
    MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
           beta_1=0.9, beta_2=0.999, early_stopping=False,
           epsilon=1e-08, hidden_layer_sizes=(15, 10, 5), learning_rate='constant',
           learning_rate_init=0.001, max_iter=200, momentum=0.9,
           nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
           solver='lbgfs', tol=0.0001, validation_fraction=0.1, verbose=False,
           warm_start=False)

    clf.predict()

elif self.technique == "SVM":
    from sklearn.svm import SVC
    clf = SVC()
    clf.fit(complete.pil)
    SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

    clf.predict()

elif self.technique == "DECISIONTREE":
     from sklearn import tree
     clf = tree.DecisionTreeClassifier()
     clf = clf.fit(complete.pil)

     clf.predict()

else:
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    clf.fit(complete.pil)

    clf.predict()
