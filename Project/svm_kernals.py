import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class kernals:
    try:
        logging.info('Implemeting svm kernals to get good accuracy')
        def polynomial_Kernal(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.svm import SVC
            sv_classifier = SVC(kernel='poly', degree=8)
            sv_classifier.fit(X_train_transformed, y_train)
            polynomial_kernal_pred = sv_classifier.predict(X_test_transformed)
            return polynomial_kernal_pred

        def rbf_Kernal(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.svm import SVC
            sv_classifier = SVC(kernel='rbf')
            sv_classifier.fit(X_train_transformed, y_train)
            rbf_kernal_pred = sv_classifier.predict(X_test_transformed)
            return rbf_kernal_pred

        def sigmoid_Kernal(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.svm import SVC
            sv_classifier = SVC(kernel='sigmoid')
            sv_classifier.fit(X_train_transformed, y_train)
            sigmoid_kernal_pred = sv_classifier.predict(X_test_transformed)
            return sigmoid_kernal_pred
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))