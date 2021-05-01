import pyautogui
import time

print(pyautogui.size()) # Bildschirm größe --> Abfragen auf welchem Bildschirm was läuft
x, y = pyautogui.size() # in Höhe und Breite unterteilen
p = pyautogui.position()
print(p) # Mausposition (one less)

# pyautogui.moveTo(10,10, duration=1.5) # Mausbewegen zu einem Punkt (wohin x, wohin y, wie lange?)
# pyautogui.moveRel(2000, 500, duration=2) # Mausbewegung von wo man ist (x, y, wie lange?)

time.sleep(2)
pyautogui.click(379, 17) # Klicken (doubleClick, rightClick)
pyautogui.displayMousePosition()