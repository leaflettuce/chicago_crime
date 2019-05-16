# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:44:34 2019

@author: andyj
"""

import os 
import pandas as pd
import numpy as np

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df = pd.read_csv('../../data/interim/aggregate_data.csv')

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


####################
### aggregation ####
####################
df['count'] = 0 # helper col
# DAILY
# # Agg daily Counts 
df_daily = df.groupby(['date'])['count'].agg('count')
df_daily['date'] = df_daily.index

# Write Out
upload_dir = 'E:/projects/chi_crime/data/processed/'
upload_file = 'daily_counts'
df_daily.to_csv(upload_dir + upload_file + '.csv', index = False)


# HOURLY
# # Agg hourly/day Counts 
df_hourly = df.groupby(['date', 'hour'])['count'].agg('count').reset_index()

# Write Out
upload_file = 'hourly_counts'
df_hourly.to_csv(upload_dir + upload_file + '.csv', index = False)

# WEEKLY
# # Agg weekly Counts 
df_weekly = df.groupby(['year', 'week_number'])['count'].agg('count').reset_index()

# Write Out
upload_file = 'weekly_counts'
df_weekly.to_csv(upload_dir + upload_file + '.csv', index = False)

# FINAL write out
df = df.drop(['count'], axis = 1)
upload_file = 'crime'
df.to_csv(upload_dir + upload_file + '.csv', index = False)