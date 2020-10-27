import requests as req
import random as rand

query = "%E5%8C%97%E6%B5%B7%E9%81%93"

r = req.get("http://geoapi.heartrails.com/api/json?method=getCities&prefecture="+query)
fetched = r.json()["response"]["location"]

cities_with_ruby = tuple((i["city"], i["city_kana"]) for i in fetched)

def ynq(prompt):
    while 1:
        stdin = input(prompt)
        if stdin not in ["y", "n"]:
            print(f"y か n を入力してください．")
            continue
        elif stdin == "y":
            return True
        else:
            return False
        

while 1:
    question = rand.choice(cities_with_ruby)
    reading = question[1]
    stdin = input(f"{question[0]} の読みは何でしょうか？ひらがなで答えてください．")
    if stdin == reading:
        print(f"正解！")
    else:
        print(f"不正解！正解は {reading} でした！")

    if ynq("もう一度遊びますか? y/n >>> "):
        print()
        continue
    else:
        print()
        print("また遊んでね！ created by: eq__s")
        print("Credit: HeartRails")
        break
