import requests
import os


res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.status_code) # Status 200 ist nice

print(len(res.text)) # Anzahl der Zeichen

print(res.text[:500]) # Printe ersten 500 Zeichen

res.raise_for_status() # gucken ob Seite existiert

playFile = open(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 12 - Web scraping\Romeo&Juliet.txt", "wb")
for chunk in res.iter_content():
    playFile.write(chunk)