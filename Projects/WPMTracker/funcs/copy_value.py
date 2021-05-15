import time, pyautogui

def copy():
    time.sleep(0.2)
    pyautogui.moveTo(950, 750)
    time.sleep(0.1)
    pyautogui.drag(-295, -250, duration=0.5, button="left")
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")