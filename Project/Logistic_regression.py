import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class logistic:
    try:
        logging.info('Implemeting logistic regession model')
        def logistic_regression(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.linear_model  import LogisticRegression
            log_regression = LogisticRegression()
            log_regression.fit(X_train_transformed, y_train)
            log_reg_pred = log_regression.predict(X_test_transformed)
            return log_reg_pred
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))