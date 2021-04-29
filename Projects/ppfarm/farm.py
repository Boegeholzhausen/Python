import pyautogui, time

# pyautogui.typewrite("Was?", interval=0.2) # Keypresses (Text, optional)
# pyautogui.press("a")


time.sleep(1) # Start Countdown

# x = pyautogui.locateCenterOnScreen(r"C:\Python\ppfarm\woodrec.png")
# print(x[0])

woodx = 1262
woody = 750
clayx = 1480
clayy = 748
ironx = 1700
irony = 747


def fill(x, y):
    pyautogui.click(x, y)
    pyautogui.typewrite("5000", interval=0.2)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter")

fill(woodx, woody)
time.sleep(6)
fill(clayx, clayy)
time.sleep(6)
fill(ironx, irony)