#!/usr/bin/env python
# coding: utf-8

# In[3]:


nums = [1, 2, 3, 4, 5]


# In[2]:


# 평균은 원소들의 합을 원소들의 개수로 나눈 값이다.


# In[4]:


# 리스트의 평균을 구하기 위해 리스트 원소들의 개수와 합을 알아야 한다.


# In[6]:


# 따라서 average를 원소들의 합인 sum(nums)와 원소들의 개수인 len(nums)로 나타내준다.
average = sum(nums) / len(nums)


# In[7]:


# 결과를 확인하기 위해 average를 print 함수의 인자로 넣어서 출력해준다.
print(average)

