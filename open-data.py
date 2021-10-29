# 網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response :
#     data=response.read().decode("utf-8") # 取得台灣大學網站原始碼 (HTML、CSS、JS)
# print(data)

# 串接、擷取公開資料
import urllib.request as request
import json
src="https://data.epa.gov.tw/api/v1/bgt_p_34?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json"
with request.urlopen(src) as response :
    data=json.load(response) # 利用 json 模組處理 json 資料格式
# 將疫苗名稱列表出來
slist=data["sort"]["fields"]
with open("data.txt","w", encoding="utf-8") as file:
    for company in slist:
        file.write(company["公司名稱"]+"\n")