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