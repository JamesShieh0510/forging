# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:41:59 2017

@author: Horace Yang
"""
import Initial as ini
import Parser_02 as par
import Featurizer_01 as far

# In[11]:
#------------------------------------------------------------------------------------------------        
if __name__ == '__main__':
       
    parm = ini.parm  # access parameters from intiial file
    
   # In[] Method A: 可輸出時間標籤
    po = par.Parser(index = parm['tNo'], timeTag = parm['timeTag'], logShow = parm['logShow'])
    s1 = po.fit_transform(parm['sFile']) # sheet name of the target file, return raw data list with time tag
    # smp = np.array(s1).astype(int)
    
    fo = far.Featurizer(timeTag = parm['timeTag'], fFile = parm['fFile'], ntype = parm['nType'], 
                     grp = parm['nGroup'], band = parm['fBand'], iOB = parm['fIOB'], 
                     mode = parm['dMode'], dur = parm['Durations'], infFactor = parm['inflection factor'],
                     sheet = '', logShow = parm['logShow']) 
    
    # fur.getInflectionPt(smp[0])
    s3 = fo.fit_transform(s1) # new miner object
    
# In[] Method B: 不可輸出時間標籤

    #from sklearn.preprocessing import Imputer
    #from sklearn.pipeline import Pipeline       
    
    #pipeline = Pipeline ([
             #('parser',   par.Parser(index = parm['tNo'], timeTag = parm['timeTag'], logShow = parm['logShow'])),
             #('imputer',  Imputer(strategy="median")),
            # ('featurize', far.Featurizer(timeTag = parm['timeTag'], fFile = parm['fFile'], ntype = parm['nType'], 
                         #grp = parm['nGroup'], band = parm['fBand'], iOB = parm['fIOB'], 
                         #mode = parm['dMode'], dur = parm['Durations'], infFactor = parm['inflection factor'],
                         #sheet = '', logShow = parm['logShow'])),
            # ])
     
    #result = pipeline.fit_transform(parm['sFile'])