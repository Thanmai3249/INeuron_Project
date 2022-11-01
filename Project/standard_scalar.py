import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)
class standardization():
    try:
        logging.info('Standardizing the data by applying standard scalar')
        def standardize_data(self, X_train, X_test):
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
            X_train_transformed = scaler.fit_transform(X_train)
            X_test_transformed = scaler.transform(X_test.values)
            print(X_train_transformed)
            return X_train_transformed, X_test_transformed
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
