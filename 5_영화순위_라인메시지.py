import urllib.request as req
from bs4 import BeautifulSoup
import requests

headers = {'Authorization': 'Bearer 본인_토큰'}  # "Bearer" 라는 글자는 지우시면 안됩니다! "
code = req.urlopen("http://www.cgv.co.kr/movies/")
soup = BeautifulSoup(code, "html.parser")
title = soup.select("strong.title")
img = soup.select("span.thumb-image > img")

for i in range(len(title)):
    print(title[i].string)
    print(img[i].attrs["src"])
    data = {"message": "{}위 : {}".format(i + 1, title[i].string),
            "imageThumbnail": img[i].attrs["src"],
            "imageFullsize": img[i].attrs["src"]}
    requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
    print()
    if i == 4:
        break
