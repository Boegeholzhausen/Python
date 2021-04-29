import bs4
import requests
import os

res = requests.get("https://10fastfingers.com/typing-test/german")

print(res.status_code)
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select("div span")
print(elems)

text = open(r"C:\Users\JannisBögeholz\Desktop\Python\automate_the_boring_stuff\Chapter 12 - Web scraping\wpm.txt", "wb")
for chunk in res.iter_content():
    text.write(chunk)