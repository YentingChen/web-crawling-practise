from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options=Options()
options.add_experimental_option('detach', True)
options.chrome_executable_path="/Users/yentingchen/Documents/VoucherCodes/pdp/python-web-crawling/chromedriver"
driver=webdriver.Chrome(options=options)
driver.maximize_window()


driver.get('https://www.vouchercodes.co.uk/')
driver.add_cookie({"name": "privacy_notice_version" , "value": "2021-1", 'path' : '/'})
driver.add_cookie({"name": "cookie_notice_version" , "value": "2019-3", 'path' : '/'})
driver.refresh()
link=driver.find_element(By.LINK_TEXT, "View All Top Offers")
link.click()
time.sleep(5) 

offers=driver.find_elements(By.TAG_NAME, "h3")
with open('offers_selenium.txt', 'w', encoding='utf-8') as file:
     for offer in offers:
         file.write(offer.text+"\n")

# driver.close()


