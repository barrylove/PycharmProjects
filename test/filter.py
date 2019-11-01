from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup


url = "http://behoimi.org/post/show/103/blonde_hair-cagalli_yula_athha-cosplay-gundam-gund"

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
html = requests.get(url)

Soup = BeautifulSoup(html.text, "lxml")
print(Soup)
img_url = Soup.find("img", id="image")
print(img_url)