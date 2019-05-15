# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:50:12 2019

@author: andyj
"""
import os

# install requirements if needed
#pip install -r ../requirements.txt

# make data directories
if not os.path.exists('../../data/raw'):
    os.mkdirs('../../data/raw')
    
if not os.path.exists('../../data/interim'):
    os.mkdir('../../data/interim')
    
if not os.path.exists('../../data/processed'):
    os.mkdir('../../data/processed')