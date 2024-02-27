from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options=Options()
options.chrome_executable_path="/Users/yentingchen/Documents/VoucherCodes/pdp/python-web-crawling/chromedriver"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.vouchercodes.co.uk/')
driver.save_screenshot("homepage_max.png")
driver.mobile()
driver.save_screenshot("homepage_min.png")
driver.close()