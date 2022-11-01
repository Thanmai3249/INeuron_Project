import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class evaluation:
    try:
        logging.info('classification evaluation metrics')
        def classification_evaluation(self,y_test, predicted):
            from sklearn.metrics import classification_report, confusion_matrix
            print(confusion_matrix(y_test, predicted))
            print(classification_report(y_test, predicted))

        def roc_auc(self,y_test, predicted):
            from sklearn.metrics import roc_auc_score
            print(roc_auc_score(y_test, predicted, multi_class="ovr"))

    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))