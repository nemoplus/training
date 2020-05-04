from time import sleep
import pyautogui

def sample(i:int):
    print(i, "start")
    pyautogui.moveTo(1, i)
    sleep(1)
    pyautogui.moveTo(1, i * 100)
    sleep(1)
    pyautogui.moveTo(i * 100, i * 100)
    sleep(1)
    pyautogui.moveTo(i * 100, 1)
    print(i, "end.")


sample(1)
sample(10)

print("Done.")

