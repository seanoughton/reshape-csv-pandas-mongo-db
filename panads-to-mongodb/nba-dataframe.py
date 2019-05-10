#!/usr/bin/env python3
import pandas as pd
import os
import pymongo
import json


data = pd.read_csv('./csv/nba.csv')



print( data.dropna(how='all').rank() )
