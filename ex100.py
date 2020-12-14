#!/usr/bin/env python
# coding: utf-8

# In[1]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]


# In[2]:


# date 리스트와 close_price 리스트를 zip해주면 0번은 0번끼리, 1번은 1번끼리 만들어진다.


# In[3]:


# 이것을 딕셔너리로 만들어주고 close_table로 지정해준다.
close_table = dict(zip(date, close_price))


# In[4]:


# 결과를 확인하기 위해 print 함수에 close_table을 인자로 넣어서 출력해준다.
print(close_table)

