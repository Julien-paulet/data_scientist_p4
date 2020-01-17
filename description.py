#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import json


# In[69]:


with open('socrata_metadata_2015-building-energy-benchmarking.json', 
          encoding="utf8") as json_file:
    data_2015 = json.load(json_file)
    
with open('socrata_metadata_2016-building-energy-benchmarking.json', 
          encoding="utf8") as json_file:
    data_2016 = json.load(json_file)


# In[79]:


df_2015 = pd.DataFrame({
    "name" : [arr["name"] for arr in data_2015["columns"]],
    "datatype" : [arr["dataTypeName"] for arr in data_2015["columns"]],
    "fieldName" : [arr["fieldName"] for arr in data_2015["columns"]],
    "desc" : [arr.get('description') for arr in data_2015['columns']]
})
df_2015 = df_2015.set_index('name')

df_2016 = pd.DataFrame({
    "name" : [arr["name"] for arr in data_2016["columns"]],
    "datatype" : [arr["dataTypeName"] for arr in data_2016["columns"]],
    "fieldName" : [arr["fieldName"] for arr in data_2016["columns"]],
    "desc" : [arr.get('description') for arr in data_2016['columns']]
})
df_2016 = df_2016.set_index('name')


# In[83]:


def search_desc(var, year):
    if year == 2015:
        desc = df_2015.loc[var, 'desc']
    elif year == 2016:
        desc = df_2016.loc[var, 'desc']
    else:
        desc = "L'année entrée n'est pas la bonne, choisir 2015 ou 2016"
    return desc

