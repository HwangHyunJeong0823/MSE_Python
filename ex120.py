#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}


# In[6]:


# "좋아하는 과일은?"을 사용자로부터 과일로 받는다.
과일 = input("좋아하는 과일은?")
# 사용자로부터 한라봉을 받았다고 하자.


# In[5]:


# 만약 사용자가 입력한 과일이 fruit 딕셔너리 안에 value 값으로 들어가있다면 "정답입니다."를 도출해준다.
if 과일 in fruit.values():
    print("정답입니다.")
# 만약 사용자가 입력한 과일이 fruit 딕셔너리 안에 value 값으로 들어가있지 않다면 "오답입니다."를 도출해준다.
else:
    print("오답입니다.")

