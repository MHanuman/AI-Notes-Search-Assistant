#!/usr/bin/env python
# coding: utf-8

# In[12]:


import json

Data={
    'rag':'Retrieval Augumented Generation',
    'llm':'Large Language Model'
}

with open("Data.json","w") as file:
    json.dump(Data,file)
    
with open("Data.json","r") as file:
    output=json.load(file)
    
topic="RAg"
print(output.get(topic.lower(),"Topic Not Found"))


# In[ ]:




