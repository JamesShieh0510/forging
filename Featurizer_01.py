# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:41:59 2017

@author: Horace Yang
"""
from sklearn.base import BaseEstimator, TransformerMixin

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft
from scipy.ndimage import gaussian_filter

class Featurizer(BaseEstimator, TransformerMixin):   
    def __init__(self, timeTag, fFile, ntype, grp, band, iOB, mode, dur, infFactor, sheet, logShow):
        self.timeTag = timeTag
        self.fw = pd.ExcelWriter(fFile, engine = 'xlsxwriter')
        self.ntype = ntype
        self.grp = grp
        self.band = band
        self.iOB = iOB
        self.mode = mode
        self.dur = dur
        self.sheet = sheet
        self.infFactor = infFactor
        self.logShow = logShow 
    
    # do nothing 
    def fit(self, X, y=None):
        return self
    
    # 轉換特徵
    def transform(self, X):
        x = self.getParsed(X) # transform X from dataframe to int array
        
        # derive overall mean, std, min, and max 
        self.xmean = x.mean()
        self.xstd = x.std()
        self.xmin = x.min()
        self.xmax = x.max()
        
        for d in range(len(self.dur)): # calculate features by duarion

            fs = [] # feature list
            for row in range(0, len(x)): # calculate all features of each duration
                t1, t2 = self.rangeFinder(x, d, row)
                if self.logShow >= 2: print('row: ', row, 't1: ', t1, 't2: ', t2) 
                
                # 正規化
                xt = x[row][t1:t2]
                xn = self.normalize(xt, ntype = self.ntype, group= self.grp) # 
                xs = pd.Series(xn)
                
                # 計算相關特徵
                xRMS = np.sqrt(np.mean(xs**2))
                xPwr = self.freqDomain(xs)
                maxvalue = max(x[row])
                features = [xs.mean(),maxvalue, xs.std(), xRMS, xs.skew(), xs.kurt()]
                for i in range(0,self.iOB,1):
                    features = features + [xPwr[i]]  # add element of list
                
                # add time tag
                if self.timeTag == True: features = [X.loc[row][0]] + features # add time to the list 
                
                fs.append(features)                
            
            fd = self.exportToSheet(fs, d)      # transform list to dataframe
        return(fd)  # return a dataframe
            
    #--------------------------------------------------------------------------------------
    def getParsed(self, X):    
    # 輸入解譯dataframe    
        signal = X              # X: dataframe
        sIndex = 1 if self.timeTag else 0             # time index: 0, data index start from 1 
        x = np.array(signal)    # x: transfer the list to array
        x = x[:,sIndex:].astype(int) # transform signals to int array
        return(x)
        
    #--------------------------------------------------------------------------------------
    def exportToSheet(self, fs, d):
    # 輸出工作表
        fd = pd.DataFrame(fs)      # transform list to dataframe
        columns = ['Mean', 'Max', 'Std', 'RMS', 'Skew', 'Kurt']
        for i in range(0,self.iOB,1): columns = columns + ['Band'+str(i)]
        if self.timeTag == True: columns = ['time'] + columns 
        if self.logShow >= 2: print(columns)
        
        fd.columns = columns
        
        # 指定輸出工作表
        if self.mode == 'I': # by the inflection point
            sn = self.sheet + '反曲 ~ 最大'
        else:
            sn = self.sheet + str(self.dur[d][0]) + ' ~ ' + str(self.dur[d][1])
                
        if self.logShow >= 2: print('export to sheet: ', sn)
        fd.to_excel(self.fw, sheet_name=sn) # write to excel    
        return(fd)
        
    #--------------------------------------------------------------------------------------
    # 計算特樣本的訊號區間
    def rangeFinder(self, x, d, row):
        if self.mode == 'R' or 'I': # relative to peak
            pIndex = np.where(x[row] == max(x[row]))  # find the time index of the max value
            offset = pIndex[0][0]                     # derive first time index with the max value
        else:
            offset = 0                                # start from time 0
        
        if self.mode == 'I': # by the inflection point
            t1 = self.getInflectionPt(x[row])
        else:
            t1 = self.dur[d][0] + offset       # get the start time index 
            
        t1 = 0 if t1< 0 else t1   
            
        t2 = self.dur[d][1] + offset       # get the end time index
        t2 = 0 if t2 < 0 else t2 
        return (t1, t2) #回傳開始與結束時間
    
    #---------------------------------------------------------------------------------------------------------
    # 正規化訊號
    def normalize(self, x, ntype, group):
        if group == 'A':  # normalize this smaple by overall 
            xmean = self.xmean; xstd = self.xstd 
            xmin = self.xmin;   xmax = self.xmax 
        else:             # normalize this sample by this sample
            xmean = x.mean();   xstd = x.std() 
            xmin = x.min();     xmax = x.max()            
        return{
            'Z': (x - xmean) / xstd, # z score
            'M': (x - xmin) / (xmax - xmin), # min-max
            'K': x  # no normalization
        }.get(ntype, x) # 
    
    #----------------------------------------------------------------------------------------------------------
    # 以FFT計算頻域能量
    def freqDomain(self, x):
        y = fft(x)
        fy = 2.0/len(y)*abs(y.real[0:int(len(y)/2)])
        maxFreq =  min(self.band * self.iOB, len(fy))
        
        py = [sum(fy[x:x+self.band]) for x in range(0, maxFreq, self.band)]
        newpy=[]
        for count  in  range(8-len(py)):
    
                newpy.insert(count,0)
        
        py = py + newpy # 補空值
        
        #print(py[0:self.iOB])
        return(py[0:self.iOB])
        
    #----------------------------------------------------------------------------------------------------------
    # 計算反曲點
    def getInflectionPt(self, x):
        # smooth out noise
        smoothed = gaussian_filter(x, 3.) # denoise
        grad = np.gradient(smoothed, 2)   # 取2次微分項
        
        std = grad.std()
        if self.logShow >= 2: 
            plt.plot(grad); plt.title('Inflection Points')
        infPt = np.where(grad > self.infFactor * std)
        return(infPt[0][0]) # return the inflection point
