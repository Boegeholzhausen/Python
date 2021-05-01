import pyautogui
import time
import pyperclip


pyautogui.moveTo(950, 750)
time.sleep(0.5)
pyautogui.drag(-295, -250, duration=0.5, button="left")
pyautogui.keyDown("ctrl")
pyautogui.press("c")
pyautogui.keyUp("ctrl")

print(pyperclip.paste())
