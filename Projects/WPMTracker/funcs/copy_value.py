import time, pyautogui

# Von der Seite kopieren und resetten
def copy():
    time.sleep(0.2)
    pyautogui.moveTo(950, 750)
    time.sleep(0.1)
    pyautogui.drag(-295, -250, duration=0.5, button="left")
    pyautogui.keyDown("ctrl")
    pyautogui.press("c")
    pyautogui.keyUp("ctrl")

    time.sleep(0.8)
    pyautogui.click(1001, 336)
    time.sleep(0.1)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.moveTo(688, 512)


# pyautogui.displayMousePosition()