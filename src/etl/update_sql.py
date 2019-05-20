# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:45:10 2019

@author: andyj
"""

import os 
import pandas as pd
import mysql.connector
import numpy as np
from mysql.connector import Error

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')
MYSQL_PASS = os.environ.get("MYSQL_PASS")

# import data
df = pd.read_csv('../../data/processed/most_recent.csv')

# oops add these back
df['latitude_2'] = 'NULL'
df['longitude_2'] = 'NULL'

# reorder cols
df_2 = pd.DataFrame(df, columns = ['arrest', 'beat', 'block', 'case_number', 'community', 'date', 'description', 'district', 'domestic', 'fbi_code',\
                                'id', 'iucr', 'latitude', 'address', 'latitude_2', 'longitude_2', 'loc_description', 'longitude', 'primary_type', \
                                'updated_on', 'ward', 'x_coord', 'y_coord', 'year', 'time', 'hour', 'month', 'day', 'hour_bin', 'day_of_week', 'week_number'])

# connect to db
cnx = mysql.connector.connect(user='root', password=MYSQL_PASS,  # set pass to API envi
                              host='localhost',
                              database='chicago_crime')
cursor = cnx.cursor()


# helpder function to insert data rows into table
def insert_crime(crime):
    query = "INSERT INTO crime(arrest, beat, block, case_number, community, date, description, district, domestic, fbi_code,\
                                id, iucr, latitude, address, latitude_2, longitude_2, loc_description, longitude, primary_type, \
                                updated_on, ward, x_coord, y_coord, year, time, hour, month, day, hour_bin, day_of_week, week_number) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
    try:
        cursor.executemany(query, crime)
 
    except Error as e:
        print('Error:', e)
 
# fix null problem
df_null = df_2.replace(np.nan, 'NULL', regex=True)

# set pandas df to list 
crimes_list = df_null.values.tolist()

# insert list into table with helper function
print('loading into SQL 10,000 rows at a time.')
for i in range(0, len(crimes_list), 10000):
    print(str(i) + '/' + str(len(crimes_list)))
    insert_crime(crimes_list[i : i + 10000])
    
cnx.commit()  # commit additions

cursor.close()