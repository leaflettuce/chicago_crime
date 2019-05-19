# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:45:10 2019

@author: andyj
"""

import os 
import pandas as pd
import mysql.connector
from mysql.connector import Error

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')
MYSQL_PASS = os.environ.get("MYSQL_PASS")

# import data
df = pd.read_csv('../../data/interim/most_recent.csv')

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
 
# set pandas df to list 
crimes_list = df.values.tolist()

# insert list into table with helper function
insert_crime(crimes_list)

cursor.close()