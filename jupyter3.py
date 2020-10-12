#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=[]
scores=set()
n=int(input())
for _ in range(n):
    name=input()
    score=float(input())
    a.append([name,score])
    scores.add(score)
second = sorted(scores)[1]
b=[]
for name,score in a:
    if score == second:
        b.append(name)
for name in sorted(b):
    print(name)


# In[4]:


import requests
response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.status_code)


# In[7]:


s=input()
print(s.swapcase())
    


# In[8]:


def swap_case(s):
    return s.swapcase()
s=input()
result = swap_case(s)
print(result)


# In[ ]:





# In[ ]:





# In[ ]:




