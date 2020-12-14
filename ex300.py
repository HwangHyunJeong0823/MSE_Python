#!/usr/bin/env python
# coding: utf-8

# In[1]:


per = ["10.31", "", "8.00"]


# In[2]:


# 기본적으로 다음과 같은 구조를 갖고 있다.
# for i in per:
    # print(float(per))


# In[3]:


for i in per:
    try:
        print(float(i))
        # 실행 코드
    except:
        print(0)
        # 예외가 발생하지 않았을 때 0이 출력된다.
    else:
        print("clean data")
        # 예외가 발생하지 않았을 때 "clean data"가 출력된다.
    finally:
        print("변환 완료")
        # 예외 발생 여부와 상관없이 항상 "변환 완료"가 출력된다.

