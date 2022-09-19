"""
Created on Thu Sep 15 11:58:33 2022

@author: Dimitris Samaras
"""


#import pandas library
import pandas as pd

#read dataset
hw = pd.read_csv("brca_cnvs_tcga-1.csv", index_col=0, parse_dates=True)

#create new variable
hw["seq_length"] = hw['loc.end'] - hw['loc.start']

#save the new dataset
hw.to_csv('output.csv')