#!/usr/bin/env python
# coding: utf-8

# In[1]:


리스트 = ["가", "나", "다", "라"]


# In[2]:


# 처음부터 끝까지 -1씩 slicing해준다.
# 한줄씩 출력되는 것을 원하기 때문에 뒤집힌 리스트에서 하나씩 프린트해준다.
for i in 리스트[::-1]:
    print(i)

