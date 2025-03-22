#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests


# In[5]:


url = "https://randomuser.me/api/?results=500"


# In[7]:


response_API = requests.get(url)


# In[9]:


print(response_API.status_code)


# In[11]:


data = response_API.json()


# In[13]:


print(data)


# In[15]:


data.keys()


# In[17]:


data['results']


# In[29]:


informations = data['results']


# In[30]:


females = []

males = []


# In[39]:


for information in informations:
    if information['gender'] == 'female': 
        females.append(information)  
    elif information['gender'] == 'male':  
        males.append(information) 


# In[41]:


print(females)


# In[43]:


print(males)


# In[71]:


for information in informations:
    print(information['dob']) 


# In[73]:


for information in informations:
    print(information['dob']['date'])


# In[77]:


dates = []


# In[79]:


for information in informations:
    dates.append(information['dob']['date']) 


# In[81]:


print(dates)


# In[87]:


for information in informations:
    print(information['name']['first'])


# In[89]:


for information in informations:
    print(information['name']['last'])


# In[97]:


full_names= []


# In[103]:


for information in informations:
    full_names.append(information['name']['first'] + " " + information['name']['last'])


# In[105]:


print(full_names)


# In[ ]:




