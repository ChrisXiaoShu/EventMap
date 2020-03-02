# 台灣政府活動地圖
## Why
台灣各縣市政府每月都有豐富的活動資源，可能是各地季節性觀光資訊、各地比賽活動、文藝休閒展覽等，其相關資訊都分散在各縣市政府，或當地旅遊網。其資源相當分散，當希望快速掌握附近活動等資訊，須在各縣市政府網站的活動年曆逐項搜尋，十分麻煩。因此希望架構一個整合各縣市政府活動資訊的網站，統一將活動訊息以地圖的方式呈現，使使用者能夠快速方便的一覽附近活動，促進國人餐與各地政府活動。  
[網頁Demo](https://chrisxiaoshu.github.io/EventMap/)  
[網頁原始碼](https://github.com/ChrisXiaoShu/EventMap)

## How
### 前端
- 使用語言
  javascript、html、css
- 部屬方式
  目前主要使用github.io架設靜態網站，後端server每周定期更新活動資訊
- [參考的前端原始碼](https://github.com/kiang/bribes_map)
- 開發相關請參考[github/wiki](https://github.com/ChrisXiaoShu/EventMap/wiki)
### 後端
- 使用python撰寫各縣市政府網站爬蟲腳本
- 部屬爬蟲腳本於GCP server
- 使用MQserver管理爬蟲工作狀態
- 開發相關請參考[github/wiki](https://github.com/ChrisXiaoShu/EventMap/wiki)
## Need
- 各縣市政府網站眾多，且各自有不同架構，須個別開發爬蟲腳本，期望能有自同道和的朋友能夠一起開發
- 本人主要擅長python跟後端架構，對前端javascript一翹不通，如有對優化前端有興趣的人歡迎憶起加入。