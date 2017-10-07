
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


dt=pd.read_csv("death.csv")


# In[28]:





# In[4]:


p=dt.keys()


# In[5]:


for i in p:
    s=re.sub(r'[^a-zA-Z0-9 ]',r'',i) 
    


# In[ ]:





# In[7]:


dt=pd.read_csv("death.csv")
dt.columns=dt.columns.str.replace('.','')
dt.columns=dt.columns.str.replace('(','')
dt.columns=dt.columns.str.replace(')','')
dt.columns=dt.columns.str.replace('  ','')
dt.columns=dt.columns.str.replace('-','')
dt.columns=dt.columns.str.replace(' ','_')
dt.columns=dt.columns.str.replace('-','_')
dt.columns=dt.columns.str.replace('No_of_Persons_Injured','_Injured_')
dt.columns=dt.columns.str.replace('No_of_Persons_Died','_Died_')
dt.columns=dt.columns.str.replace('No_of_Cases','_Cases_')
dt.columns=dt.columns.str.replace('Collapse_of_Structure','COS_')
dt.columns=dt.columns.str.replace('Drowning_Accidental_Falls_into_Waterbody','Drowing_from_falling')
dt.columns=dt.columns.str.replace('Dwelling_House/Residential_building','Residential')
dt.columns=dt.columns.str.replace('Official/Commercial_Building','Commercial')
dt.columns=dt.columns.str.replace('Accidental_Explosion_','')
dt.columns=dt.columns.str.replace('Armed_Forces/Police/CPMF','Law_agencies')
dt.columns=dt.columns.str.replace('Falls_from_Vehicles_Automobile_like_Bus,_Trucks,_etc','Falls_from_Bus/Trucks')
dt.columns=dt.columns.str.replace('Accidental_Fire_Cooking_Gas_Cylinder/Stove_Burst','Cooking_Gas_Cylinder/Stove_Burst')
dt.columns=dt.columns.str.replace('Accidental_Fire_Electrical_Short_Circuit','Short_Circuit_Fire')
dt.columns=dt.columns.str.replace('__','_')
dt.columns=dt.columns.str.replace('___','_')
dt.columns=dt.columns.str.replace('__','_')


# In[8]:


f=dt.keys()
for i in f:
    print(i)


# In[10]:


dt = dt.drop(dt.index[29])
dt = dt.drop(dt.index[-2])
dt = dt.drop(dt.index[-1])


# In[11]:


i=0
states = ['AP','AR','AS','BR', 'CT', 'GA', 'GJ','HR', 'HP', 'JK', 'JR', 'KA', 'KL', 'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OR',
         'PB', 'RJ', 'SK', 'TN', 'TL', 'TR', 'UT', 'UP', 'WB', 'AN', 'CH', 'DN', 'CT', 'LD', 'DL', 'PY']

# List of ISO recognized codes for Indian States and UTs.

for name in dt['State/UT_Name']:
    dt = dt.replace(name, states[i])
    i=i+1


# In[12]:


dt.to_csv('death_clean.csv')


# In[ ]:




