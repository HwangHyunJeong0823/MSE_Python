#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 곱셈을 위해 초기값을 1로 설정해준다.
result = 1
# 1부터 11까지의 숫자에서 result는 result가 가리키는 값에 i가 가리키는 값을 곱해준다.
for i in range(1, 11):
    result = result * i
# 결과값을 확인하기 위해 print 함수의 인자에 result를 넣고 출력해준다.
print(result)

