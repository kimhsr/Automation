from selenium import webdriver
import time
import chromedriver_autoinstaller

hash_tag = input("해시태그 입력 >> ")

chrome_path = chromedriver_autoinstaller.install()
browser = webdriver.Chrome(chrome_path)
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)

id = browser.find_element_by_name("username")
id.send_keys("본인_아이디_입력")
pw = browser.find_element_by_name("password")
pw.send_keys("본인_비밀번호_입력")
browser.find_element_by_css_selector("div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
time.sleep(4)

url = "https://www.instagram.com/explore/tags/{}/".format(hash_tag)
browser.get(url)
time.sleep(4)
# 첫번째 사진 클릭
browser.find_element_by_css_selector("div._9AhH0").click()
time.sleep(4)
# 자동 좋아요 시작
while True:
    like = browser.find_element_by_css_selector("section.ltpMr.Slqrh span > svg._8-yf5")
    value = like.get_attribute("aria-label")
    next = browser.find_element_by_css_selector("div.l8mY4.feth3 > button.wpO6b")
    if value == "좋아요": # 좋아요가 안눌려 있다면?
        like.click()
        time.sleep(30)
        next.click()
        time.sleep(30)
    elif value == "좋아요 취소": # 좋아요가 눌려있다면?
        next.click()
        time.sleep(30)


while (True):
    pass
