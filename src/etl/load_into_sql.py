# -*- coding: utf-8 -*-
"""
Created on Sun May 19 06:33:15 2019

@author: andyj
"""
import os 
import pandas as pd
import mysql.connector
from mysql.connector import Error
import numpy as np

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')
MYSQL_PASS = os.environ.get("MYSQL_PASS")

# import data
df = pd.read_csv('../../data/processed/crime.csv')

# connect to db
cnx = mysql.connector.connect(user='root', password=MYSQL_PASS,  # set pass to API envi
                              host='localhost')
cursor = cnx.cursor()

# create new DB for storage
cursor.execute("CREATE DATABASE chicago_crime")

# check it
print('checking list of DB\'s.. chicago_crime should be in list.')
cursor.execute("SHOW DATABASES") 
for i in cursor:
    print(i)
    
cursor.execute('USE chicago_crime;')

# create table for crime data
cursor.execute("CREATE TABLE crime (arrest VARCHAR(255), beat VARCHAR(64), block VARCHAR(255), \
                                    case_number VARCHAR(255), community VARCHAR(255), \
                                    date VARCHAR(255), description VARCHAR(255), \
                                    district VARCHAR(255), domestic VARCHAR(255), fbi_code VARCHAR(255), \
                                    id INT(64) PRIMARY KEY, iucr VARCHAR(255), latitude VARCHAR(255), \
                                    address VARCHAR(255), latitude_2 VARCHAR(255), longitude_2 VARCHAR(255), \
                                    loc_description VARCHAR(255), longitude VARCHAR(255), primary_type VARCHAR(255), \
                                    updated_on VARCHAR(255), ward VARCHAR(255), x_coord VARCHAR(255), y_coord VARCHAR(255), \
                                    year INT(64), time TIME, hour INT(64), month INT(64), day INT(64), \
                                    hour_bin VARCHAR(255), day_of_week VARCHAR(255), week_number INT(64))")

# check it
print('checking list of table\'s.. crime should be only one.')
cursor.execute("SHOW TABLES") 
for i in cursor:
    print(i)

# helpder function to insert data rows into table
def insert_crime(crime):
    query = "INSERT INTO crime (arrest, beat, block, case_number, community, date, description, district, domestic, fbi_code,\
                                id, iucr, latitude, address, latitude_2, longitude_2, loc_description, longitude, primary_type, \
                                updated_on, ward, x_coord, y_coord, year, time, hour, month, day, hour_bin, day_of_week, week_number) \
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            
    try:
        cursor.executemany(query, crime)
 
    except Error as e:
        print('Error:', e)


# fix null problem
df_null = df.replace(np.nan, 'NULL', regex=True)

# set pandas df to list 
crimes_list = df_null.values.tolist()
# crimes_list = crimes_list[:100]   # for testing

# insert list into table with helper function
print('loading into SQL 10,000 rows at a time.')
for i in range(0, len(crimes_list), 10000):
    print(i + '/' + len(crimes_list))
    insert_crime(crimes_list[i : i + 10000])
    
# commit additions
cnx.commit()

# test query - for testing
#cursor.execute('SELECT * FROM chicago_crime.crime \
#               LIMIT 100;')
#for result in cursor:
#    print(result)

cursor.close()