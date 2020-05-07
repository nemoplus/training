from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

from bs4 import BeautifulSoup as bs

import chromedriver_binary

options = webdriver.ChromeOptions()
#options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("http://www.python.org")


while True:
    print(driver.current_url)

    val = input('Q:exit > ')

    if val == "Q":
        break

    if val == "l":
        for i in bs(driver.page_source).find_all('form'):
            for j in i.find_all('input')
                print(j)

    if val == "q":
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)


driver.close()
