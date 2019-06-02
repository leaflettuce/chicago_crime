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