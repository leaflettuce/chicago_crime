# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:57:37 2019

@author: andyj
"""
import os 
import pandas as pd
import statsmodels.api as sm
import itertools
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df = pd.read_csv('../../data/processed/weekly_counts.csv')
df.head()


############
# PREPPING #
############

# add interval column
df['order'] = df.index + 1

# drop week 53 rows  
df = df[df.week_number != 53]

# drop unneeded cols
df_split = df[['order', 'count']]


# initial visual eda
df_split['count'].plot(figsize=(15, 6))
plt.show()

# split test and train   850 - 111 (17 years - two years)
df_train = df_split.iloc[:850,:]
df_test = df_split.iloc[850:, :]



############
# MODELING #
############

######### FROM tutorial on digital ocean
# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 52) for x in list(itertools.product(p, d, q))]
############ END tutorial

