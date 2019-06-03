# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 09:13:55 2019

@author: andyj
"""

import os 
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pylab as plt
plt.style.use('fivethirtyeight')


# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df = pd.read_csv('../../data/processed/weekly_counts.csv')
df.head()

# reset index to overall week number
df = df[df.week_number != 53]
df = df.reset_index()
df['order'] = df.index + 1
df.index = df.order
series = df['count']

# quick visualize
plt.plot(series)      # NOTE - Series is additive - not need to log!

# split test and train
df_train = series[:850]
df_test = series[850:]

# set differencing period
df_train_diff = df_train.diff(periods=1).values[1:]

###############
# EVAL SERIES #
###############
# plot it out to check
plt.plot(df_train_diff)
plt.title('differential over time')
plt.xlabel('weeks')
plt.ylabel('crime rate differential')

# get diff stats
lag_acf = acf(df_train_diff, nlags = 120)
lag_pacf = pacf(df_train_diff, nlags = 120, method = 'ols')

# splot acf
plt.figure(figsize=(15,5))
plt.subplot(121)
plt.stem(lag_acf)
plt.axhline(y=0, linestyle='-', color = 'black')
plt.axhline(y=-1.96/np.sqrt(len(df_train)), linestyle='--', color = 'grey')
plt.axhline(y=1.96/np.sqrt(len(df_train)), linestyle='--', color = 'grey')
plt.xlabel('lag')
plt.ylabel('acf')

# plot pacf
plt.subplot(122)
plt.stem(lag_pacf)
plt.axhline(y=0, linestyle='-', color = 'black')
plt.axhline(y=-1.96/np.sqrt(len(df_train)), linestyle='--', color = 'grey')
plt.axhline(y=1.96/np.sqrt(len(df_train)), linestyle='--', color = 'grey')
plt.xlabel('lag')
plt.ylabel('pacf')
plt.tight_layout()

## Season = 52 p=1, q=1, d=1 //  ACF, p = 1 // pacf, q = 1 or 2 or 3   
# SARIMA((1,2), 1, (1,2,3)) (1,1,1)52

#########
# MODEL #
#########
# fit model
model = SARIMAX(df_train, order = (1, 1, 2), seasonal_order = (1, 0, 1, 52), 
                enforce_stationarity=False, enforce_invertibility=False)

model_fit = model.fit(disp=False)

# forecast it out
forecast_len = len(df_test)
forecast = model_fit.forecast(forecast_len)

# eval metrics
rmse = np.sqrt(((forecast - df_test) ** 2).mean())
p_rmse = (rmse / df_test.mean())*100

# plot it again
plt.figure(figsize=(20,10))
plt.plot(series, 'b')
plt.plot(forecast, 'r')

plt.title('RMSE: %.2f     Percent Avg Error: %.2f'%(rmse, p_rmse))
plt.xlabel('Weeks')
plt.ylabel('Weekly Rates')
plt.autoscale(enable=True, axis = 'x', tight=True)
plt.axvline(x=series.index[len(df_train)], color='black')

# write out for testing
df_test.to_csv('../../data/processed/test_actuals.csv')

forecast.to_csv('../../data/processed/test_forecasted.csv')

##############
# prediction #
##############
# predict out for 52
model = SARIMAX(series, order = (1, 1, 2), seasonal_order = (1, 0, 1, 52), 
                enforce_stationarity=False, enforce_invertibility=False)

model_fit = model.fit(disp=False)

# forecast it out
forecast = model_fit.forecast(52)   #.predicted_mean
forecast.to_csv('../../data/processed/arima_2_preds.csv')