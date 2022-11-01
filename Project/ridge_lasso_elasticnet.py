import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class regularization:

    try:
        logging.info('Implementing regularization techniques to improve the performance')

        # Implementing ridge regression
        def ridge_regression(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.linear_model import Ridge
            ridge_reg = Ridge(alpha=0.1)
            ridge_reg.fit(X_train_transformed,y_train)
            ridge_pred =ridge_reg.predict(X_test_transformed)
            return ridge_pred

        # Implementing Lasso Regression
        def lasso_regression(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.linear_model import Lasso
            lasso_reg = Lasso(alpha=0.1)
            lasso_reg.fit(X_train_transformed,y_train)
            lasso_pred = lasso_reg.predict(X_test_transformed)
            return lasso_pred

        # Implementing elasticnet regression
        def elasticnet_regression(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.linear_model import ElasticNet
            en_reg = ElasticNet(random_state=0)
            en_reg.fit(X_train_transformed,y_train)
            en_pred = en_reg.predict(X_test_transformed)
            return en_pred

    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
