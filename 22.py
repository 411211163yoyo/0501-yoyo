import requests
from bs4 import BeautifulSoup
url = "https://www.atmovies.com.tw/movie/next/"
Data = requests.get(url)
Data.encoding = "utf-8"
#print(Data.text)
sp = BeautifulSoup(Data.text, "html.parser")
result=sp.select(".filmListAllX li")
for item in result:
print(item)
print()
img = item.find("img")
  #print("片名:", img.get("alt"))
  #print("海報:", img.get("src"))
  a = item.find("a")
  #print("介紹:", "http://www.atmovies.com.tw" + a.get("href"))
  #print("編號:", a.get("href")[7:19])
  div = item.find(class_="runtime")
  #print("日期:", div.text[5:15])
  if div.text.find("片長：")>0:
  FilmLen =div.text[21:]
  #print("片長：", div.text[21:])
  else:\
    FilmLen ="無"
  # print("目前無片長資訊")
  doc = {
    "title": img.get("alt"),
    "hyperlink": "http://www.atmovies.com.tw" + a.get("href"),
    "picture": img.get("src"),
    "showDate": div.text[5:15],
    "showLength": FilmLen
    }
   doc_ref = db.collection("楊子青").document(a.get("href")[7:19])
   doc_ref.set(doc)
   return"資料庫已更新"

   if __name__ == "__main__"
   app.run()
