import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)
class encoding:
    try:
        logging.info('Encoding using label encoder')
        def label_encoding(self, imputed_df):
            from sklearn.preprocessing import LabelEncoder
            imputed_df = imputed_df.select_dtypes(include = 'object')
            encoder = LabelEncoder()
            for c in imputed_df.columns:
                imputed_df[c] = encoder.fit_transform(imputed_df[c])
            return imputed_df
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))
