from selenium import webdriver
import time
import chromedriver_autoinstaller
import os

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net")
id = browser.find_element_by_css_selector("#id")
id.send_keys("본인 아이디 입력")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("본인 비밀번호 입력")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("카페 주소 입력")
time.sleep(3)
# 중고나라 게시판 클릭
browser.switch_to.frame(browser.find_element_by_css_selector("#down"))  # 프레임 전환
browser.find_element_by_css_selector("#fldlink_rRa6_347").click()
time.sleep(3)

try:
    f = open("./중고나라.txt", "r")
    ref = f.readlines()
except:
    f = open("./중고나라.txt", "w")
    ref = []
f.close()

# 게시판 제목 크롤링
title = browser.find_elements_by_css_selector("a.txt_item")
new_one = 0
for i in title:
    if (i.text + "\n") not in ref:  # 새로운 올라온 글이라면?
        with open("./중고나라.txt", "a") as f:
            f.write(i.text + "\n")
        if "노트북" in i.text:
            new_one += 1

print("{} 관련 글이 {} 개 올라왔습니다.".format("노트북", new_one))
browser.close()

if new_one >= 1:
    from twilio.rest import Client

    account_sid = 'TWILIO_ACCOUNT_SID' # SID 입력
    auth_token = 'TWILIO_AUTH_TOKEN' # 토큰 입력
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body="{} 관련 글이 {} 개 올라왔습니다.".format("노트북", new_one),
             to='+8210xxxxxxxx', # 본인 번호 입력
             from_="+17752529488" # 발급 받은 번호 입력

         )
