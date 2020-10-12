#!/usr/bin/env python
# coding: utf-8

# In[1]:


def split_join(line):
    a=line.split(" ")
    a='-'.join(a)
    return a
line=input()
result=split_join(line)
print(result)


# In[2]:


def mutate_string(string,position,character):
    a=list(string)
    a[position]=character
    string="".join(a)
    return string
string= input()
position,character= input().split()
result=mutate_string(string,int(position),character)
print(result)


# In[ ]:




