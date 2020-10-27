import requests as req
import random as rand

query = "%E5%8C%97%E6%B5%B7%E9%81%93"

r = req.get("http://geoapi.heartrails.com/api/json?method=getCities&prefecture="+query)
cities = r.json()["response"]["location"]
cities = tuple(i["city"] for i in cities)
print(rand.choice(cities))
