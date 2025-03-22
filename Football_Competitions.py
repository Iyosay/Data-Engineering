#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests


# In[5]:


url = "http://api.football-data.org/v4/competitions/"


# In[7]:


response_API = requests.get(url)


# In[9]:


print(response_API.status_code)


# In[11]:


football_data = response_API.json()


# In[13]:


print(football_data)


# In[15]:


football_data.keys()


# In[17]:


football_data['competitions']


# In[19]:


competition_names_list = []


# In[21]:


for competition in football_data['competitions']:
    name = competition['name']
    competition_names_list.append(name) 


# In[57]:


print(competition_names_list)


# In[31]:


print(len(competition_names_list))


# In[25]:


distinct_competition_names = set(competition_names_list)


# In[27]:


competition_names = list(set(competition_names_list))


# In[29]:


print(competition_names)


# In[33]:


print(len(competition_names))


# In[ ]:




