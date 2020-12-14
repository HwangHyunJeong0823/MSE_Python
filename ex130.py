#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']


# In[2]:


# print 함수에 btc를 인자로 넣어서 출력해주고 값을 확인한다.
print(btc)


# In[3]:


# btc가 딕셔너리라는 것을 알 수 있다.


# In[4]:


# 최고가는 btc에서 max_price에 접근해주고, 최저가는 btc에서 min_price에 접근해준다.
최고가 = btc['max_price']
최저가 = btc['min_price']


# In[6]:


# 계산을 위해 최고가, 최고가의 타입, 최저가, 최저가의 타입을 print 함수를 사용해 출력해준다.
print(최고가, type(최고가))
print(최저가, type(최저가))


# In[7]:


# 더하기, 빼기를 하기 위해 float해준다.
최고가 = float(btc['max_price'])
최저가 = float(btc['min_price'])
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])


# In[8]:


# 만약 시가+변동폭이 최고가보다 크다면 상승장을 출력해주고, 그렇지 않다면 하락장을 출력해준다.
# if와 else 조건문을 사용해준다.
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

