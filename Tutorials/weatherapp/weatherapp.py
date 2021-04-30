import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = r"https://weather.com/de-DE/wetter/10tage/l/Paderborn+Nordrhein+Westfalen?canonicalCityId=89ff5896683eea17a6becd09bdf428c6a18c8bfa88dc6ccff00dfeb2d1839ead"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open(r"C:\Python\Tutorials\weatherapp\img_weather.jpg")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)


def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find("span", class_="LocationPageTitle--PresentationName--Injxu").text
    temperature = soup.find("span", class_="DailyContent--temp--_8DL5").text
    weatherprediction = soup.find("p", class_="DailyContent--narrative--3AcXd").text

    locationLabel.config(text=location)
    temperaturLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherprediction)

    temperaturLabel.after(60000, getWeather)
    master.update()

locationLabel = Label(master, font=("Calibri bold", 20), bg = "white") #styles
locationLabel.grid(row=0, sticky="N", padx=100) #posi

temperaturLabel = Label(master, font=("Calibri bold", 70), bg = "white") #styles
temperaturLabel.grid(row=1, sticky="W", padx=40) #posi

Label(master, image=img, bg="white").grid(row=1, sticky="E") # img positionieren (wo?, image=was?, bg?, ).grid(row=?, sticky="W")

weatherPredictionLabel = Label(master, font=("Calibri bold", 15), bg="white")
weatherPredictionLabel.grid(row=2, sticky="W", padx=40)

getWeather()

master.mainloop()