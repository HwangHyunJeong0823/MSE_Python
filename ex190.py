#!/usr/bin/env python
# coding: utf-8

# In[1]:


apart = [ [101, 102], [201, 202], [301, 302] ]


# In[3]:


# apart 리스트에 1층, 2층, 3층별로 리스트가 있고, 그 리스트 안에 집이 정해져있다.
# 각 집의 호수를 출력해준다.
for 층 in apart:
    for 집 in 층:
        print(집, "호")
# 아파트 단지를 다 돌았으니 마지막 줄에 "-----"를 출력해준다.
print("-----")

