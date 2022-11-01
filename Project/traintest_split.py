import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class split:
    try:
        logging.info('splitting data to train and test data')
        def data_split(self, X, y):
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
            #print(len(X_train), len(y_test))
            return(X_train, X_test, y_train, y_test)
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))