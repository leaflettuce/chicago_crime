# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 08:22:14 2019

@author: andyj
"""

import os 
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# setwd
os.chdir('E:/projects/chi_crime/src/etl/')

# import
df = pd.read_csv('../../reports/NEXT_WEEKS_PRED_MATRIX.csv')

# map community numnber to area name

# visualize