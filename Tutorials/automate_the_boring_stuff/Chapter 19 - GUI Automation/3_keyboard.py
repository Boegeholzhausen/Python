import pyautogui

pyautogui.click(1900, 500)
pyautogui.typewrite("Was?", interval=0.2) # Keypresses (Text, optional)
pyautogui.typewrite(["a", "b", "left", "X", "Y"], interval=1)
print(pyautogui.KEYBOARD_KEYS)

pyautogui.press("a")