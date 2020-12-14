#!/usr/bin/env python
# coding: utf-8

# In[1]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]


# In[3]:


volatility = []
# i를 사용해서 0, 1, 2, 3, 4까지의 숫자를 만들어준다.
for i in range(5):
# 변동폭은 high_prices의 i번째 원소에서 low_prices의 i번째 원소를 빼준 것이다.
    diff = high_prices[i] - low_prices[i]
# 그리고 이 변동폭을 volatility 리스트에 저장해주어야 하므로 for문 바깥쪽에 비어있는 리스트를 만들어준 후 for문에서 리스트를 지정해준다.
    volatility.append(diff)


# In[4]:


# 결과를 확인하기 위해 print 함수에 volatity를 인자로 넣어 출력해준다.
print(volatility)

