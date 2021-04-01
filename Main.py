from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, os
url = "https://trends.google.com/trends/trendingsearches/daily?geo=TW"

# set webdriver and setting, and only support ver 89 or late by 20210402


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


# browser = webdriver.Chrome(options=chrome_options, executable_path="/Users/loic/Workspace/selenium/chromedriver")

browser.get(url)
# set waiting condition
condition = EC.visibility_of_all_elements_located((By.CLASS_NAME, "md-list-block"))
wait = WebDriverWait(browser, 3).until(condition)
WebDriverWait(driver=browser, timeout=3, poll_frequency=0.1)

# soup's work
soup = BeautifulSoup(browser.page_source, "lxml")
browser.quit()

data = {'trending': []}

# keyword = []
# detail = []
# when = []
# count = []

md_list = soup.find_all("md-list")
md_list.pop(0)
for i in md_list:
    # 寫 find_all 下面的 find 才找得到我也不知道為什麼
    for j in i.find_all(class_="details", limit=1):
        keyword_soup = j.find(class_="title").find("a").string.strip()
        detail_soup = j.find(class_="summary-text").find("a").string
        when_soup = j.find(class_="source-and-time").find("span").find_next("span").string.strip().replace("h ago", " 小時前")
        count_soup = j.find(class_="subtitles-overlap").find("div").string.strip().replace("searches", "筆搜尋").replace("0K", "萬").replace("K", "000")
        # print(keyword +detail + when +  count)
        # print(keyword + " " + detail + " " + when + " " + count)
        data['trending'].append({'keyword': keyword_soup, 'detail': detail_soup, 'when': when_soup, 'count': count_soup})
        # keyword.append(keyword_soup)
        # detail.append(detail_soup)
        # when.append(when_soup)
        # count.append(count_soup)
# for i in range(0,20):
#     data['trending'].append({'keyword': keyword[i], 'detail': detail[i], 'when': when[i], 'count': count[i]})


def result():
    return json.dumps(data, indent=1, ensure_ascii=False)
# send =
# return send
# print(send)




