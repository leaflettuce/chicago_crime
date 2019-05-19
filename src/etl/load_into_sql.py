# -*- coding: utf-8 -*-
"""
Created on Sun May 19 06:33:15 2019

@author: andyj
"""
import os 
import pandas as pd
import mysql.connector

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')
MYSQL_PASS = os.environ.get("MYSQL_PASS")

# import data
df = pd.read_csv('../../data/processed/crime.csv')

# connect to db
cnx = mysql.connector.connect(user='root', password=MYSQL_PASS,  # set pass to API envi
                              host='localhost',
                              database='chicago_crime')
cursor = cnx.cursor()



#### test query##########################
# query = ("SELECT * FROM sales")
#
# write out results
# cursor.execute(query)
# for i in cursor:
#    print(i)
#########################################