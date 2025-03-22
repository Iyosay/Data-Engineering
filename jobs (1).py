#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[3]:


url = "https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo"


# In[5]:


response_API = requests.get(url)


# In[7]:


print(response_API.status_code)


# In[9]:


print(response_API)


# In[11]:


get_data = response_API.json()


# In[13]:


print(get_data)


# In[15]:


print(get_data.keys())


# In[17]:


job_data = get_data['jobs']


# In[19]:


len(get_data['jobs'])


# In[21]:


job_data[0]


# In[23]:


job_data[0]['jobTitle']


# In[25]:


senior_role_list = []


# In[27]:


manager_role_list = []


# In[29]:


for jobs in job_data:
    role_list = jobs['jobTitle']
    if "Senior" in role_list:
        print(role_list)


# In[34]:


for jobs in job_data:
    if 'Senior' in jobs['jobTitle']:  
        senior_role_list.append(jobs['jobTitle'])
    if 'Manager' in jobs['jobTitle']: 
        manager_role_list.append(jobs['jobTitle']) 


# In[36]:


print(senior_role_list)


# In[38]:


print(manager_role_list)

