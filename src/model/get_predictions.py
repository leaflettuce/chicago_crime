# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 08:26:31 2019

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

# reset index to overall week number
df = df[df.week_number != 53]
df = df.reset_index()
df['order'] = df.index + 1
df.index = df.order
series = df['count']
series = series[:-1]

#########
# MODEL #
#########
# predict out for 52
model = SARIMAX(series, order = (1, 1, 2), seasonal_order = (1, 0, 1, 52), 
                enforce_stationarity=False, enforce_invertibility=False)

model_fit = model.fit(disp=False)

# forecast it out
forecast = model_fit.forecast(24)   #.predicted_mean
forecast.to_csv('../../data/processed/predictions.csv')
 

# visualize

# visualize forecast
# Get forecast 24 steps ahead in future
pred_uc = model_fit.get_prediction(start=len(series), end=len(series)+24, dynamic=True, full_results=True)
pred_ci = pred_uc.conf_int()

year_pred = pred_uc.predicted_mean


# pplot them out
series_cut = series[-104:]
ax = series_cut.plot(label='Actual', figsize=(20, 15))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Week')
ax.set_ylabel('Weekly Rates')
plt.title('Weekly Crime Rates for Chicago', fontsize = '32')
plt.axvline(x=len(series), color='black', linewidth = '2.5')
plt.text(x=len(series)+.5, y=6250, s='Today', fontsize=14)
plt.legend()
plt.show()

# write it
plt.savefig('../../reports/visuals/updated/6m-forecast.png')


# getg pred matrix
pred_table = pd.read_csv('../../data/processed/prop_table_edit.csv', index_col = 0)
preds = forecast.reset_index(drop=True)
next_week_pred = preds[1]
pred_table *= next_week_pred
pred_table = np.round(pred_table, 0)

# write out prediction table
pred_table.to_csv('../../reports/NEXT_WEEKS_PRED_MATRIX.csv')
