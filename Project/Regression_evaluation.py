import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class evaluation_metrics:
    try:
        logging.info('REgression evaluation metrics')
        def reg_evaluation(self, y_test, predicted, X_test):
            print('MSE - ',mean_squared_error(y_test,predicted))
            print('MAE - ',mean_absolute_error(y_test,predicted))
            print('RMSE - ',np.sqrt(mean_absolute_error(y_test, predicted)))
            score = r2_score(y_test, predicted)
            print('R2 - ',score)
            print('Adjusted R2 - ', 1-(1-score)*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))