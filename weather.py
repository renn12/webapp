# coding:utf-8
import json
import requests

params = {"version": "1", "city": "부산", "county": "수영구", "village": "광안동"}
headers = {"appKey": "1a9892f6-585f-3520-b651-9e7ee4472831"}
r = requests.get("http://apis.skplanetx.com/weather/current/hourly", params=params, headers=headers)

data = json.loads(r.text)
weather = data["weather"]["hourly"]
cTime = weather[0]["timeRelease"]
cSky = weather[0]["sky"]["name"]
cWind = weather[0]["wind"]["wspd"]
cTemp = weather[0]["temperature"]["tc"]

cWeather = "오늘의 날씨"+ cTime+" 기즌 하늘은 "+cSky+"이고 풍속은 "+cWind+"이고 기온은 "+cTemp+"입니다."
print(cWeather)
#print(r.json())


# json 인코딩
jsonString = json.dumps(data)
print(jsonString)
print(type(jsonString))

# json 디코딩
dict = json.loads(jsonString)
print(dict)
