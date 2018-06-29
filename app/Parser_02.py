# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:38:32 2017

@author: Horace Yang
"""

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.base import BaseEstimator, TransformerMixin
# 解譯原始訊號檔，並轉成 Dataframe 與 解譯檔
class Parser(BaseEstimator, TransformerMixin):
    def __init__(self, index, timeTag, logShow):
        self.index = index
        self.timeTag = timeTag
        self.logShow = logShow # 顯示過程?
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        sFile = X
        fr = pd.read_csv(sFile, header = 0, encoding = 'big5')  # read raw data in csv 
        tTime = self.index[0]  # time tag index of the csv file
        tNo = self.index[1]    # start index of the rawdata in the csv file 

        raw = [] # new list       
        for row in range(0,len(fr.index)):
            ls = fr.loc[row][tNo].split(',')  # split raw data by row
            if self.logShow >= 1: plt.plot(ls)
            if self.timeTag == True:
                ls.insert(0,fr.loc[row][tTime])   # insert time tag at first location of list
            raw.append(ls)
            
        # Write your DataFrame to a file
        if self.logShow >= 1: plt.title('Source Signal'); plt.show() #
        tData = pd.DataFrame(raw)      # transform list to dataframe
        return(tData) # return a dataframe

