# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:23:29 2019

@author: andyj
"""

import os 
import pandas as pd

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df_agg = pd.DataFrame()
for year in range(2001, 2020): # iterate through each year, pulling in raw data and adding to final aggregate df
    temp_df = pd.read_csv('../../data/raw/raw_' + str(year) + '.csv')
    if year == 2001:
        df_agg = temp_df
    else:
        df_agg = pd.concat([df_agg, temp_df])
        
df_agg = df_agg.reset_index(drop=True)      
 
# check it
df_agg.head()
df_agg.tail()

# write out
upload_dir = 'E:/projects/chi_crime/data/interim/'
upload_file = 'aggregate_data'
df_agg.to_csv(upload_dir + upload_file + '.csv', index = False)