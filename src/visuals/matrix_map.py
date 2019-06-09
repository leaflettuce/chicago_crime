# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 08:22:14 2019

@author: andyj
"""

import os 
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

# setwd
os.chdir('E:/projects/chi_crime/src/visuals/')

# import
df = pd.read_csv('../../reports/NEXT_WEEKS_PRED_MATRIX.csv', index_col = 'Community Area')

# map community numnber to area name
comm_numbers = np.array([i for i in range(1, 78)]) # get comm numbers

comm_names = np.array(['fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill', # get names (in order))
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill',
                       'fill', 'fill', 'fill', 'fill', 'fill', 'fill', 'fill'])

connector_df = pd.DataFrame({'numbers' : comm_numbers, 'names' : comm_names}) # create df

# replace df community area number with name
# DO THIS NEXT

# visualize
plt.figure(figsize=(20,40))
sns.heatmap(df, annot=True, linewidths=.5, cmap="Reds", vmin = 0, vmax = 10, cbar=False)
plt.yticks(rotation=0)
           
# write it
plt.savefig('../../reports/visuals/updated/pred_matrix.png')