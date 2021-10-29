# 載入 pandas 模組
import pandas as pd
# 建立 Series
data=pd.Series([20,10,15])
# 基本 Series 操作
# print(data) 印出 data 內容
# print("Max",data.max()) 印出最大值
# print("Medium",data.median()) 印出中位數
# data=data*2 資料都*2
# print(data)
# data=data==20
# print(data)


# 建立 DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Cena"],
    "salary":[30000,50000,40000]
})
# 基本 DataFrame 操作
# print(data)
# 取的特定欄位
# print(data["name"])
# 取的特定的列
print(data)
print("=================")
print(data.iloc[1])