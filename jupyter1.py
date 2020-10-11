#!/usr/bin/env python
# coding: utf-8

# In[1]:


print ("hello world")


# In[2]:


i=1 
while i<=10:
    print(i)
    i=i+1


# In[25]:


def operations(num1,num2,operator):
    if(operator == '+'):
        result= num1+num2
        print(result)
    elif(operator == '-'):
        result= num1-num2
        print(result)
    elif(operator == '*'):
        result= num1*num2
    elif(operator == '//'):
        result= num1//num2
    elif(operator =='%'):
        result= num1%num2
    elif(operator=='/'):
        result= num1/num2
    else:
        result=0
    print("Answer: {} : ({},{}) : result={}" .format(operator,num1,num2,result))
operations(5,2,'//')


# In[ ]:





# In[ ]:




