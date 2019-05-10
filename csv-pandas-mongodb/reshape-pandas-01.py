#!/usr/bin/env python3
import pandas as pd
import os
import pymongo
import json

mng_client = pymongo.MongoClient('localhost', 27017)
# // Replace mongo db name
mng_db = mng_client['test_data_reshape']
collection_name = 'customer_price_reshape_02' #// Replace mongo db collection name
db_cm = mng_db[collection_name]
# cdir = os.path.dirname(__file__)
# filepath = 'reshape_data_01.xlsx'
# file_res = os.path.join(cdir, filepath)

data = pd.read_excel('reshape_data_01.xlsx',0)
data_reshape = pd.pivot_table(data, values='value',index=['customer','quantity'],columns=['product'])

print(data.info())


# # data_reshape.to_csv('example',index=False)
# data_json = json.loads(data_reshape.to_json(orient='records'))
#
# # print(data_json)
# db_cm.remove()
# db_cm.insert(data_json)
#
# ex_data = pd.read_excel('reshape_data_01.xlsx',0)
# ex_data_reshape = pd.pivot_table(ex_data, values='value',index=['customer','quantity'],columns='product')

# print(ex_data_reshape)
