# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 12:57:37 2019

@author: andyj
"""
import os 
import pandas as pd
import statsmodels.api as sm
import itertools
import math
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


# drop week 53 rows  
df = df[df.week_number != 53]
df = df.reset_index()

# add interval column
df['order'] = df.index + 1
df.index = df['order']

# drop unneeded cols
df_split = df[['order', 'count']]


# initial visual eda
df_split['count'].plot(figsize=(15, 6))
plt.show()

# split test and train   850 - 111 (17 years - two years)
df_train = df_split.iloc[:850,:]
df_test = df_split.iloc[850:, :]
df_train.head()


############
# MODELING #
############

######### FROM tutorial on digital ocean  <------ ORIGINAL GRID SEARCH
# Define the p, d and q parameters to take any value between 0 and 2
#p = d = q = range(0, 2)

# Generate all different combinations of p, q and q triplets
#pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
#seasonal_pdq = [(x[0], x[1], x[2], 52) for x in list(itertools.product(p, d, q))]

# Run through grid search using AIC as eval metric
#for param in pdq:
#    for param_seasonal in seasonal_pdq:
#        try:
#            mod = sm.tsa.statespace.SARIMAX(df_train['count'],
#                                            order=param,
#                                            seasonal_order=param_seasonal,
#                                            enforce_stationarity=False,
#                                            enforce_invertibility=False)#
#
#            results = mod.fit()
#
#            print('ARIMA{}x{}52 - AIC:{}'.format(param, param_seasonal, results.aic))
#        except:
#            continue


# Fit model to best AIC scoring parameters 
mod = sm.tsa.statespace.SARIMAX(df_train['count'],
                                order=(1, 1, 1),
                                seasonal_order=(1   , 1, 1, 52),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()
print(results.summary().tables[1])
############ 


##############
# Evaluation #
##############
results.plot_diagnostics(figsize=(15, 12))
plt.show()


# set to test data
pred = results.get_prediction(start=851, end=955,dynamic=True, full_results=True)
pred_ci = pred.conf_int()

# map out actual and forecast on plot
ax = df_split['count'].plot(label='Actual', figsize=(20, 15))
pred.predicted_mean.plot(label='Forecast', ax=ax)
## fill
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
# background
ax.fill_betweenx(ax.get_ylim(), 851, 955,
                 alpha=.1, zorder=-1)

ax.set_xlabel('Date')
ax.set_ylabel('Weekly Crime Rates')

plt.legend()
plt.show()

# test forecast and get MSE
y_forecasted = pred.predicted_mean
y_truth = df_test['count']

# Compute the mean square error
rmse = math.sqrt(((y_forecasted - y_truth) ** 2).mean())
print('The Root Mean Squared Error of our forecasts is {}'.format(round(rmse, 2)))

p_rmse = rmse / y_truth.mean()
print('Forecaster is off by an average of {}% each week.)'.format(round(p_rmse*100, 1)))

###################
# forecasting out #
###################

# Get forecast 52 steps ahead in future
pred_uc = results.get_prediction(start=955, end=1047, dynamic=True, full_results=True)
#pred_uc = results.get_forecast(steps=52)
year_pred = pred_uc.predicted_mean
year_pred.to_csv('../../data/processed/arima_1_preds.csv')
# Get confidence intervals of forecasts
pred_ci = pred_uc.conf_int()

# pplot them out
ax = df_split['count'].plot(label='Actual', figsize=(20, 15))
pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)
ax.set_xlabel('Date')
ax.set_ylabel('Weekly Rates')

plt.legend()
plt.show()