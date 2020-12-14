#!/usr/bin/env python
# coding: utf-8

# In[1]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']


# In[4]:


# 방법1


# In[3]:


# 리스트의 원소가'.h'나 '.c'로 끝나면 출력해준다.
for i in 리스트:
    if i.endswith(('.h', '.c')):
        print(i)


# In[6]:


# 방법2


# In[8]:


# 리스트의 원소를 '.'을 기준으로 분리해준다.
# 만약 확장자가 'h'이거나 'c'이면 i를 출력해준다.
for i in 리스트:
    name, ext = i.split('.')
    if ext == 'h' or ext == 'c':
        print(i)

