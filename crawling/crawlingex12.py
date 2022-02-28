#step1.관련 패키지 import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import requests
import time

#step2.검색할 키워드 입력
query = input('검색할 키워드를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
url = 'https://www.naver.com/'
s = Service("C:\ph\PYTHONexam\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(url)
time.sleep(3)

#step4.검색창에 키워드 입력 후 엔터
search_box = driver.find_element(By.ID, "query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

#step5.뉴스 탭 클릭
driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/ul/li[8]/a').click()
time.sleep(2)

#step5.검색 결과 페이지에서 selenium 패키지로 수집해보기
"""news_titles = driver.find_elements_by_css_selector(".news_tit")

for i in news_titles:
    title = i.text
    print(title)
    print()
"""

#step5-1.검색 결과 페이지의 html 문서 전체를 받아와서 bs4로 파싱하여 수집하기

for index in range(2, 11):
    html = driver.page_source
    soup = bs(html, 'html.parser')
    titles = soup.select('a.news_tit')
    for i in titles:
        title = i.get_text()
        print(title)
    print()
    if index > 6:
        driver.find_element(By.XPATH, f'//*[@id="main_pack"]/div[2]/div/div/a[6]').click()
    else:
        driver.find_element(By.XPATH,  f'//*[@id="main_pack"]/div[2]/div/div/a[{index}]').click()
