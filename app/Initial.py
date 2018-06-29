# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:41:59 2017

@author: Horace Yang
"""

DATA_ROOT =""
DATA_PATH = "ex/"

parm = {
 #-------------------------------------------------------------------------
    # show the log message or not?
    'logShow' :0,  # {0, 1, 2}, 0: no log, 1: basic logs, 2: detail 

 #----------------------------------------------------------------------------------------       
    # 訊號來源處理    
    'sFile': DATA_ROOT+DATA_PATH+'Exp1_d4.csv',     # raw signal file name (訊號來源檔)
    'tNo': [0, 1],      # tNo[0]: index of time tag, tNo[1]: index of signal data (訊號來源檔欄位定義)
    
    'timeTag': True,   # {False, True}, save time tag or not?   (解譯檔是否存時間欄位)

    'pFile': DATA_ROOT+DATA_PATH+'Parsedtest.csv',      # parsed data file name (解譯檔)
    'sRate': 1000,      # sampling rate of original signal  (訊號來源檔之訊號取樣頻率)
    
      # for plot
    'pPeriod': 1,       # display duratio time in sec  (訊號顯示時間間格)
    'pSample': 10,      # no of samples for plotting   (訊號顯示最大樣本數)        
    
 #------------------------------------------------------------------------------------------   
    # 訊號特徵化處理
    'fFile': DATA_ROOT+DATA_PATH+'Exp1_d4(1).xlsx',   # feature file name     (特徵檔)
    
      # for feature extarction
    'nType': 'K',    # {'Z', 'M', 'K'}, 'Z': z transform, 'M': max-min, 'K'; keep original (正規化方式)
    'nGroup': 'A',   # {'A', 'S'}, 'A': overall, 'S': by sample  (正規化群組)
    
     # signal durations 
    'dMode': 'I',    # {'I', 'R', 'A'}, 'I': Inflection to Max, 'R': Relative, 'A': Absolute  (擷取訊號方式:相對或絕對)
    
    'Durations': [[-50, 0]], # (擷取訊號時間區間), 若dMode用'I'僅能指定一區間; 'R''A'不限定
                            # ex. 'R':[[-150,-100], [-100, -50],[-50, 0]]; 'I': [[-50,0]]
    'inflection factor': 1.2, # 大於此反曲點標準差倍率，則認定為反曲點
        
     # features of frequency domain 
    'fBand': 5,         # spectrum size of each frequency band (擷取訊號之FFT頻帶寬度)
    'fIOB': 8 ,         # Frequency Interesting of Bands  (擷取訊號之FFT最大頻帶數)
    }
