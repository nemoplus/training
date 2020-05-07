from selenium import webdriver
import chromedriver_binary
from bs4 import BeautifulSoup as bs


options = webdriver.ChromeOptions()
#options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://qiita.com')

print(driver.current_url)

html = driver.page_source

soup = bs(html)

print(soup.prettify())

input('wait...')

driver.quit()



