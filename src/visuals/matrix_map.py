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

comm_names = np.array(['Rogers Park', 'West Ridge', 'Uptown', 'Lincoln Square', 'North Center', 'Lake View', 'Lincoln Park', # get names (in order))
                       'Near North Side', 'Edison Park', 'Norwood Park', 'Jefferson Park', 'Forest Glen', 'North Park', 'Albany Park',
                       'Portage Park', 'Irving Park', 'Dunning', 'Montclair', 'Belmont Cragin', 'Hermosa', 'Avondale',
                       'Logan Square', 'Humbolt Park', 'West Town', 'Austin', 'West Garfield Park', 'East Garfield Park', 'Near West Side',
                       'North Lawndale', 'South Lawndale', 'Lower West Side', 'Loop', 'Near South Side', 'Armour Square', 'Douglas',
                       'Oakland', 'Fuler Park', 'Grand Boulevard', 'Kenwood', 'Washington Park', 'Hyde Park', 'Woodlawn',
                       'South Shore', 'Chatham', 'Avion Park', 'South Chicago', 'Burnside', 'Calumet Heights', 'Roseland',
                       'Pullman', 'South Deering', 'East Side', 'West Pullman', 'Riverdale', 'Hedgewisch', 'Garfield Ridge',
                       'Archer Heights', 'Brighton Park', 'McKinley Park', 'Bridgheport', 'New City', 'West Edison', 'Gage Park',
                       'Clearing', 'West Lawn', 'Chicago Lawn', 'West Englewood', 'Englewood', 'Greater Grand Crossing', 'Ashburn',
                       'Auburn Gresham', 'Beverly', 'Washington Heights', 'Mount Greenwood', 'Morgan Park', 'O\'Hare', 'Edgewater'])

connector_df = pd.DataFrame({'numbers' : comm_numbers, 'names' : comm_names}) # create df


# replace df community area number with name
connector_df.index = connector_df.numbers # map out

df['name'] = connector_df.names # add to df
df.index = df.name # replace index
df = df.drop(['name'], axis = 1) # drop helper


# visualize
plt.figure(figsize=(30,60))
sns.heatmap(df, annot=True, linewidths=.5, cmap="Reds", vmin = 0, vmax = 10, cbar=False)
plt.yticks(rotation=0)
plt.title('Predicted Crime Rates for Chicago Neighborhoods by 8-Hour Blocks (3/9 - 3/15)')
           
# write it
plt.savefig('../../reports/visuals/updated/pred_matrix.png')