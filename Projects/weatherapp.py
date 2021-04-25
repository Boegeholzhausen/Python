import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = r"https://weather.com/de-DE/wetter/10tage/l/Paderborn+Nordrhein+Westfalen?canonicalCityId=89ff5896683eea17a6becd09bdf428c6a18c8bfa88dc6ccff00dfeb2d1839ead"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.openr(r"C:\Python\Projects\")