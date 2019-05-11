# -*- coding: utf-8 -*-
"""
Created on Fri May 10 08:06:51 2019

@author: andyj
"""
import requests
import os 
import sys
import json
from pandas.io.json import json_normalize 

########################
# contacts epxloration #
########################

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?"

API_TOKEN = os.environ.get("CHI_API_TOKEN")
if not API_TOKEN:
    print("You need to get an City of Chicago API token! Exiting..")
    sys.exit(1)
    
# set parameters
param = {'$$app_token' : API_TOKEN,
         #'$select' : 'date, COUNT(date)',   #example query
         #'$group' : 'date',    # example query
         '$limit' : '1000000',
         '$where' : 'year = 2009'}
  
# API call 
response = requests.get(URL, params = param)
data = json.loads(response.text)

# set to df
df = json_normalize(data)

#drop cols
df.drop(df.columns[0:8], axis = 1, inplace = True)

# write out
upload_dir = 'E:/projects/chi_crime/data/raw/'
upload_file = 'test'
df.to_csv(upload_dir + upload_file + '.csv', index = False)