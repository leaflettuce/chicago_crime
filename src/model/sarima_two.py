# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:13:55 2019

@author: andyj
"""

import os 
import pandas as pd
import statsmodels.api.statespace.sarimax as SARIMA
import matplotlib.pylab as plt
plt.style.use('fivethirtyeight')


# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df = pd.read_csv('../../data/processed/weekly_counts.csv')
df.head()

# reset index to overall week number
df['order'] = df.index + 1
df.index = df.order
series = df['count']

# quick visualize
plt.plot(series)      # NOTE - Series is additive - not need to log!


# split test and train
df_train = series[:850,:]
df_test = series[850:, :]

# set differencing period
df_train_diff = df_train.diff(periods=1).values[1:]

# plot it out to check

