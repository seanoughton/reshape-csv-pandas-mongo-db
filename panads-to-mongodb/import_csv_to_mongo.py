
#!/usr/bin/env python
import os
import pandas as pd
import pymongo
import json



def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    # // Replace mongo db name
    mng_db = mng_client['mongodb_name']
    collection_name = 'zoo' #// Replace mongo db collection name
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)



if __name__ == "__main__":
  filepath = 'zoo.csv'  #// pass csv file path
  import_content(filepath)
