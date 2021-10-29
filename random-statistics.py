# 隨機模組
import random
# 隨機選取
# data=random.choice([1,5,8,9,10,90]) # choice 隨機取一
# data=random.sample([1,5,8,9,10,90], 3) # sample 隨機取多
# data=[1,5,8,20]
# random.shuffle(data) # 隨機調換 (洗牌)
# print(data)

# 隨機取得亂數
# data=random.random() # 0 ~ 1 之間的隨機亂數
# data=random.uniform(60,100)
# print(data)

# 取得常態分配亂數
# 平均數 100, 標準差 10, 得到的資料多數在 90 ~ 110 之間
# data=random.normalvariate(100, 10)

# 平均數 0，標準差 5，得到的資料【多數】在 -5 ~ 5 之間
# data=random.normalvariate(0, 5)
# print(data)

# 統計模組
# import statistics as stat
# data=stat.mean([1,4,5,8]) # mean 平均數
# data=stat.median([1,4,5,8,100]) # median 中位數
# data=stat.stdev([1,2,3,4,5,8,10]) # stdev 標準差
# print(data)