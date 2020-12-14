#!/usr/bin/env python
# coding: utf-8

# In[1]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]


# In[5]:


# 시가에 매수해서 종가에 매도했을 때 수익금은 시가와 종가의 차이이다.
# 각 거래일의 수익금: 시가 - 종가
# 3일동안 거래를 했을 때 총 수익금을 구해준다.

total_profit = 0    # 초기 총 수익금을 0으로 지정해준다.

for day_price in ohlc[1:]:    # for문을 사용해서 총 수익금을 알아낼 것이다.
    profit = day_price[0] - day_price[3]    # 수익금 = 시가 - 종가
    total_profit = total_profit + profit    # 총 수익금에 현재 수익금을 더해주는 것이다.

# 마지막으로 총 수익금의 결과값을 print 함수를 사용해서 출력해준다.
print(total_profit)

