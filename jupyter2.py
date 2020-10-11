#!/usr/bin/env python
# coding: utf-8

# In[3]:


n=int(input())
integer_list= map(int,input().split())
t=tuple(integer_list)
print(hash(t))


# In[4]:


x,y,z,n = int(input()), int(input()), int(input()),int(input())         #or use for_ in range(4)
print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n])


# In[ ]:


a=[]
scores =set()
for _ in range(int(input())):
    name = input()
    score = float(input())
    a.append([name,score])
    scores.add(score)
second=sorted(scores)[1]
b=[]
for name,score in a:
    if score == second:
        b.append(name)
for name in sorted(b):
    print(name)


# In[ ]:





# In[ ]:




