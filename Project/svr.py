import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class support_vector_regressor:
    try:
        logging.info('Implemeting support vector regession model')
        def svm_regressor(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.svm import SVR
            sv_regressor = SVR()
            sv_regressor.fit(X_train_transformed, y_train)
            svr_pred = sv_regressor.predict(X_test_transformed)
            return svr_pred
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
