from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import requests

#요즘 핫한 번역 서비스 파파고에 접속하여 (https://papago.naver.com/) ‘i love koala study’ 라는 문장을 번역하도록 해보세요.
url = "https://papago.naver.com/"
s = Service("C:\ph\PYTHONexam\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(url)
time.sleep(2)

translate = driver.find_element(By.ID, "txtSource")
translate.send_keys("i love Python study")
driver.find_element(By.XPATH, '//*[@id="btnTranslate"]/span[1]').click()
time.sleep(2)

html = driver.page_source
soup = bs(html, 'html.parser')
korean = soup.select_one("div#txtTarget")
print(korean.string)






