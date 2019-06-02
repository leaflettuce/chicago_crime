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
import warnings
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


# set to test data   <- HERE!
pred = results.get_prediction(start=850, dynamic=True, full_results=True)
pred_ci = pred.conf_int()

ax = df.count[850:].plot(label='observed', figsize=(20, 15))
pred.predicted_mean.plot(label='Dynamic Forecast', ax=ax)

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.25)

ax.fill_betweenx(ax.get_ylim(), 850, 955,
                 alpha=.1, zorder=-1)

ax.set_xlabel('Date')
ax.set_ylabel('CO2 Levels')

plt.legend()
plt.show()

# test forecast and get MSE
y_forecasted = pred.predicted_mean
y_truth = y[851:]

# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))