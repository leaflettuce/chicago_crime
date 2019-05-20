# -*- coding: utf-8 -*-
"""
Created on Mon May 20 07:58:09 2019

@author: andyj
"""


import os 
import pandas as pd
import numpy as np

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df = pd.read_csv('../../data/interim/most_recent.csv')

##########################
### Feature Generation ###
##########################

# set time
df['time'] = ''
df.time = df.date.str[11:-7]

# set date
df['full_date'] = df.date
df.date = df.date.str[0:10]

# set hours
df['hour'] = 0
df.hour = df.time.str[0:2].astype(int)

# set month
df['month'] = df.date.str[5:7].astype(int) 

# set day of month
df['day'] = df.date.str[8:10].astype(int) 

# set hour bins
conditions = [
    (df['hour'] >= 0) & (df['hour'] < 8),
    (df['hour'] >= 8) & (df['hour'] < 16),
    (df['hour'] >= 16)]
choices = ['0 - 8', '8 - 16', '16 - 24']
df['hour_bin'] = np.select(conditions, choices, default='0')

# add day of week
df['datetime'] = pd.to_datetime(df.date) # helper col
df['day_of_week'] = df['datetime'].dt.day_name()

# add week number
df['week_number'] = df['datetime'].dt.week

# Prune features
df = df.drop(['datetime', 'full_date'], axis = 1) # drop helper


# Write Out
upload_dir = 'E:/projects/chi_crime/data/processed/'
upload_file = 'most_recent'
df.to_csv(upload_dir + upload_file + '.csv', index = False)