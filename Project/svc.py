from sklearn.svm import SVC
import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class support_vector_classifier:
    try:
        logging.info('Hyper parameter tuning')
        def svm_classifier(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.svm import SVC
            sv_classifier = SVC()
            # model fitting
            sv_classifier.fit(X_train_transformed, y_train)
            # Prediction
            svc_pred = sv_classifier.predict(X_test_transformed)
            return svc_pred

        def hyperparameter_tuning(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.model_selection import GridSearchCV
            # defining parameter range
            param_grid = {'C': [0.1, 1, 10, 100, 1000],
            'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
            'kernel': ['rbf']}
            grid = GridSearchCV(SVC(), param_grid, refit = True, verbose = 3)

            # fitting the model for grid search
            grid.fit(X_train_transformed, y_train)
            # Predicting
            grid_predictions = grid.predict(X_test_transformed)
            return grid_predictions
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))