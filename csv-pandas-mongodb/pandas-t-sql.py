import pandas as pd
import os
import pymongo
import json

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("postgres://localhost/mydb")

if not database_exists(engine.url):
    create_database(engine.url)




data = pd.read_excel('reshape_data_01.xlsx',0)
data_reshape = pd.pivot_table(data, values='value',index=['customer','quantity'],columns=['product'])

print(data_reshape)

data_reshape.to_sql(
    name='customers', # database table name
    con=engine,
    if_exists='append',
    index=True
)
