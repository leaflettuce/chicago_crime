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


# DAILY
# # Agg daily Counts 
# # Write Out

# HOURLY
# # Agg hourly/day Counts 
# # Write Out

# SPECIFIC
# Remove unneeded for time-series, set interval, and write out (interval and rate only)

# Agg split on ward and write