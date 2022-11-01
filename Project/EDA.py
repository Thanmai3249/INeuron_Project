import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging
from sklearn.impute import SimpleImputer

# Creating logging file
logging.basicConfig(filename='log_file.log',level = logging.INFO)

class data:
    try:
        logging.info('Loading excel or csv file')
        def load_data(self, path):
            if path.endswith(".csv"):
                df = pd.read_csv(path)
            elif path.endswith('.xlsx'):
                df = pd. read_excel(path)
            return df
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

    try:
        logging.info('checking for null values and imputing with Most-Frequent value')    
        def check_null(self, df):   # works for both numerical and categorical data
            null_values = df.isnull().sum().sum()
            if null_values == 0:
                print('No null values exist')
            else:
                from sklearn.impute import SimpleImputer
                #imputing with most frequent values
                imputer = SimpleImputer(strategy='most_frequent', missing_values=np.nan)
                imputer = imputer.fit(df)
                imputed_df = pd.DataFrame(imputer.transform(df.loc[:,:]), columns = df.columns)
                return imputed_df
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))    

    try:
        logging.info('Performing data analysis')
        def data_analysis(self,imputed_df):
            print(imputed_df.info())
            # Central tendencies
            print(imputed_df.describe().T)
            # Graphical analysis of each column
            # plt.figure(figsize=(20,25), facecolor='white')
            # plotnumber = 1
            # for column in imputed_df:
            #     if plotnumber<=9 :
            #         ax = plt.subplot(3,3,plotnumber)
            #         sns.kdeplot(data[column])
            #         plt.xlabel(column,fontsize=20)
            #     plotnumber+=1
            # plt.show()
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))


    try:
        logging.info('Outlier detection')
        def outliers(self, imputed_df):
            for column in imputed_df:
                plt.figure(figsize=(17,1))
                sns.boxplot(data=imputed_df, x=column)
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))


    try:
        logging.info('Pickling')
        def pickling(self,imputed_df):
            import pickle 
            #store obj
            with open(imputed_df,"wb") as o:
                pickle.dump(data,o)

            # for load data
            with open('filename', 'rb')  as o:
                Objdata=pickle.load(o)
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

# path = r"C:\Users\Thanmai\INEURON\Admission.xlsx"
# obj = data()
# df = obj.load_data(path)
# df = obj.check_null(df)
    



