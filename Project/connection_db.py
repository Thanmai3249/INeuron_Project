import pymongo
import json
import logging

logging.basicConfig(filename='log_file.log',level = logging.INFO)

class database:
    try:
        logging.info('Loading imputed data to Mongodb')
        def connecting_mongodb(self,imputed_df, path, table_name, database_name):
            import pymongo
            client = pymongo.MongoClient("mongodb+srv://Thanmai1998:Thanmai@thanmai.oczr5.mongodb.net/?retryWrites=true&w=majority")
            db = client.test
            print(db)
            imputed_df.to_json('Income_data_json.json')
            with open(path) as file:
                data = json.load(file)
            mydb = client[database_name]
            mycol = mydb[table_name]
            mycol.insert_one(data)
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex)) 

    try:
        logging.info('Fetching data from Mongodb')
        def fetch_data(self, table_name, database_name):
            client = pymongo.MongoClient("mongodb+srv://Thanmai1998:Thanmai@thanmai.oczr5.mongodb.net/?retryWrites=true&w=majority")
            # Database Name
            db = client[database_name]
            # Collection Name
            col = db[table_name]
            x = col.find()
            for data in x:
                # print(data)
                return data
    except Exception as ex:
        logging.exception("The exception that we have got:" + "\n" + str(ex))

    


# database.connecting_mongodb(df, path)
# mydb = myclient["Project"]
# mycol = mydb["Elcectricity_consumption"]
# mycol.insert_many(mylist)

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as pd
# import seaborn as sns
# from EDA import data
# from standard_scalar import standardization
# from sklearn.model_selection import train_test_split
# from traintest_split import split
# from connection_db import database
# from sklearn.linear_model import LinearRegression
# from ridge_lasso_elasticnet import regularization
# from Regression_evaluation import evaluation_metrics
# from Linear_regression import lr

# path = r"C:\Users\Thanmai\INEURON\Electricity_consumption.xlsx"
# obj = data()
# df = obj.load_data(path)
# imputed_df = obj.check_null(df)
# obj2 = database()
# obj2.connecting_mongodb(imputed_df)
