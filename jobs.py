#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests


# In[4]:


url = "https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo"


# In[5]:


response_API = requests.get(url)


# In[6]:


print(response_API.status_code)


# In[7]:


print(response_API)


# In[8]:


get_data = response_API.json()


# In[9]:


print(get_data)


# In[10]:


print(get_data.keys())


# In[11]:


get_data['jobs']


# In[12]:


senior_role_list = []


# In[13]:


manager_role_list = []


# In[ ]:


for jobTitle in get_data['jobs']:
    senior_role_list = get_data['jobs']
    senior_role_list.append(jobTitle) 


# In[ ]:


print(senior_role_list)


# In[ ]:


for jobTitle in get_data['jobs']:
    manager_role_list = get_data['jobs']
    manager_role_list.append(jobTitle) 


# In[ ]:


print(manager_role_list)

