import pyautogui, time


# Excel Öffnen [easy]
def open_easy():
    pyautogui.keyDown("winleft")
    pyautogui.press("r")
    pyautogui.keyUp("winleft")
    time.sleep(0.05)
    pyautogui.typewrite("wpm.xlsx", interval=0.01)
    pyautogui.press("enter")

# Excel Öffnen [hard]
def open_hard():
    pyautogui.keyDown("winleft")
    pyautogui.press("r")
    pyautogui.keyUp("winleft")
    time.sleep(0.05)
    pyautogui.typewrite("hwpm.xlsx", interval=0.01)
    pyautogui.press("enter")