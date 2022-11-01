from EDA import data
from standard_scalar import standardization
from sklearn.model_selection import train_test_split
from traintest_split import split
from sklearn.linear_model import LinearRegression
from ridge_lasso_elasticnet import regularization
from Regression_evaluation import evaluation_metrics
import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)


class lr:
    try:
        logging.info('Implemeting Linear Regression Model')
        def linear_regression(self, X_train_transformed, y_train, X_test_transformed, y_test):
            from sklearn.linear_model import LinearRegression
            linear_regression = LinearRegression()
            # model fitting
            linear_regression.fit(X_train_transformed, y_train)
            # Predicting
            linear_reg_pred = linear_regression.predict(X_test_transformed)
            return linear_reg_pred
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))


# path = r"C:\Users\Thanmai\INEURON\Admission.xlsx"
# obj = data()
# df = obj.load_data(path)
# print('.............................Loaded Dataset Successfully..............................')
# obj.check_null(df)
# print('.............................Done Checking for Null Values..............................')
# print('.............................Done Checking for Outliers..............................')
# X = df.drop('Chance_of_Admit_', axis = 1)
# y = df['Chance_of_Admit_']
# obj3 = split()
# X_train, X_test, y_train, y_test = obj3.data_split(X,y)
# print('.............................Done Splitting Data..............................')
# obj4 = standardization()
# X_train_transformed, X_test_transformed = obj4.standardize_data(X_train, X_test)
# print('.............................Done Standardization..............................')
# obj5 = lr()
# linear_reg_pred = obj5.linear_regression(X_train_transformed, y_train, X_test_transformed, y_test)
# print('.............................Implemented Linear Regression Successfully..............................')
# obj6 = regularization()
# ridge_pred = obj6.ridge_regression(X_train_transformed, y_train, X_test_transformed, y_test)
# lasso_pred = obj6.lasso_regression(X_train_transformed, y_train, X_test_transformed, y_test)
# en_pred = obj6.elasticnet_regression(X_train_transformed, y_train, X_test_transformed, y_test)
# print('.............................Implemented Regularization Techniques Successfully..............................')
# obj7 = evaluation_metrics()
# print('Evaluating Linear Regression Model')
# obj7.reg_evaluation(y_test, linear_reg_pred, X_test)
# print('Evaluating Ridge Regression Model')
# obj7.reg_evaluation(y_test, ridge_pred, X_test)
# print('Evaluating Lasso Regression Model')
# obj7.reg_evaluation(y_test, lasso_pred, X_test)
# print('Evaluating Elastic Net Regression Model')
# obj7.reg_evaluation(y_test, en_pred, X_test)