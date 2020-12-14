#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 방법1


# In[7]:


data = [2, 4, 3, 1, 5, 10, 9]
# sort를 사용하면 정렬이 되는데, 기본적으로 오름차순으로 정렬이 된다,
data.sort()
# 결과를 확인하기 위해 data를 print 함수의 인자로 넣어 출력해준다.
print(data)
# 이때 원본 데이터가 변경되는 것이다.


# In[9]:


# 방법2


# In[10]:


data = [2, 4, 3, 1, 5, 10, 9]
# sorted 함수에 data라는 리스트를 부여해준다.
data2 = sorted(data)
# 원본 리스트는 그대로 있고 data2를 통해서 오름차순으로 정렬된 결과를 확인할 수 있다,
# 결과를 확인하기 위해 data2를 print 함수의 인자로 넣어 출력해준다.
print(data2)

