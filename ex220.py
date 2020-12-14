#!/usr/bin/env python
# coding: utf-8

# In[1]:


# def로 print_max(a,b,c)를 지정해줄 것이다.
def print_max(a,b,c) :
# a라는 변수, b라는 변수, c라는 변수가 어떤 값을 각각 바인딩할 것이다.
    # 만약에 a가 b보다 크고 a가 c보다도 크면 a가 가장 크다.
    if a>b and a>c:
        print(a)
    # 만약 그렇지 않고 b가 c보다 크고 b가 a보다 크면 b가 가장 크다.
    elif b>c and b>a:
        print(b)
    # 그렇지도 않으면 c가 가장 크다.
    else:
        print(c)


# In[2]:


# 만약 (0,30,20)에서의 가장 큰 수를 출력하면 30이 나와야 한다.
print_max(0,30,20)

