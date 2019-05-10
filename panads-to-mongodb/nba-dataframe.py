#!/usr/bin/env python3
import pandas as pd
import os
import pymongo
import json


data = pd.read_csv('./csv/nba.csv')

data['sport']  = 'basketball'
data["Weight in Kg"] = data["Weight"].mul(0.5)
data.dropna(subset=["Salary"], inplace=True)

data['Salary'].fillna(value=0,inplace=True)
data['College'].fillna(value='No College',inplace=True)


print( data.dropna(how='all').rank() )
