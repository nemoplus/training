from selenium import webdriver
import chromedriver_binary

## Yahoo!のトップページを開く
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.yahoo.co.jp/')

"""
## 「天気・災害」のリンクを開く
x,y = pyautogui.locateCenterOnScreen('weather.png')
pyautogui.moveTo(x, y)
pyautogui.click(x, y)

## 週間予報が表示されるように少し縦にスクロールする
pyautogui.vscroll(-5)

## 範囲を指定して週間予報の部分のスクリーンショットを取得する
screenshot = pyautogui.screenshot(region=(225, 225, 650, 450))
screenshot.save('yahoo_weather.png')
"""

driver.quit()
