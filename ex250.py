#!/usr/bin/env python
# coding: utf-8

# In[3]:


# for i in range(0, 5): 를 해주면 기본적으로 정수 단위로 증가한다.


# In[4]:


# numpy라는 모듈에 arange를 사용해서 0.1씩 증가하게 해줘야 한다. 


# In[5]:


import numpy
for i in numpy.arange(0, 5, 0.1):
    # i 값을 출력해준다.
    print(i)

