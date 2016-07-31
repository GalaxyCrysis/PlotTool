import mysql.connector
from mysql.connector import Error
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import pandas as pd

def getMYSQL(user, password, host, port, database, table, method):
    try:
        conn = mysql.connector.connect(host=host, database=database,user= user,password=password)
        if conn.is_connected():
            if method is "all":
                #pandas method to get dataframe
                df = pd.read_sql("SELECT * FROM " + table, con=conn)
                return df
            else:
                df = pd.read_sql(method, con=conn)
                return df
    except Error as err:
        return ("Error: " + str(err))

def getMONGODB(user, password, host, port, database, table, method):
    try:
        #connect with database
        if user and password:
            mongo_uri = "mongodb://%s:%s@%s:%s/%s" %(user,password,host,port,database)
            client = MongoClient(mongo_uri)
        else:
            client = MongoClient(host, port)

        #get database
        db = client[database]
        #get table(collection)


        #get data from collection
        if method =="all":
            #get all data
            cursor = db[table].find()
            #put in dataframe
            df = pd.DataFrame(list(cursor))
            #delete the _id
            del(df["_id"])

            return df
        else:
            cursor = db[table].find(method)
            df = pd.DataFrame(list(cursor))
            del(df["_id"])
            return df


    except ConnectionFailure as err:
        message = "Error: " + str(err)
        return message







