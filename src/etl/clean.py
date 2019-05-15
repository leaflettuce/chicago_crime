# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:44:34 2019

@author: andyj
"""

import os 
import pandas as pd

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df = pd.read_csv('../../data/interim/aggregate_data.csv')

df.updated_on

# set date
df['date'] = ''
df.date = df.updated_on.str[0:10]

# set time
df['time'] = ''
df.time = df.updated_on.str[11:-7]

df['hour'] = 0
df.hour = df.time.str[0:2].astype(int)

# bin out hours
def set_hour_bin(hour):
    if hour >= 0 & hour < 8:
        return '0 - 8'
    elif hour >= 8 & hour < 16:
        return '8 - 16'
    else:
        return '16-24'

df['hour_bin'] = ''
df.hour_bin = df.hour.apply(set_hour_bin)

 # TO DO
 
# CLEAN
# split date and time
# split date into month and day
# get day of week
# write out standard

# DAILY
# # Agg daily Counts 
# # Write Out

# SPECIFIC
# # # Remove unneeded for time-series, set interval, and write out (interval and rate only)
# # # Tableau file?
# # # Agg split on neighborhood and write
# # # Agg split on crime type and write