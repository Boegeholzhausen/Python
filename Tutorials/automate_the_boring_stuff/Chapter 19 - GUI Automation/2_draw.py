import pyautogui, time

time.sleep(2)
pyautogui.click()    # Click to make the window active.
distance = 600
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.1)   # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.1)   # Move down.
    pyautogui.drag(-distance, 0, duration=0.1)  # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.1)  # Move up.