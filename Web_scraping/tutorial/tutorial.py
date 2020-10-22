import requests
from bs4 import BeautifulSoup

r = requests.get("https://newspicks.com/")
data = BeautifulSoup(r.text, "html.parser")
heads = data.find_all("div", class_="title _ellipsis")

for item in heads:
    print(item.getText())

