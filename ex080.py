#!/usr/bin/env python
# coding: utf-8

# In[4]:


# 범위를 나타내기 때문에 range 함수를 사용한다.


# In[3]:


# 2부터 99까지 2의 간격으로 나타내준다.
a = range(2, 99, 2)


# In[5]:


# 아직 range로 나타나있기 때문에 튜플로 받아준 후 print 함수의 인자로 넣어 출력해준다.
print(tuple(a))

