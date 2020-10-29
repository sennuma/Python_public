from random import choice
from urllib import parse

import requests as req

query: str = parse.quote("沖縄県")

r = req.get(
    "http://geoapi.heartrails.com/api/json?method=getCities&prefecture=" + query
)
fetched: dict = r.json()["response"]["location"]

# cities with ruby
cwr: list = [(i["city"], i["city_kana"]) for i in fetched]


def ynq(prompt: str) -> bool:
    while 1:
        stdin: str = input(prompt)
        if stdin not in ["y", "n"]:
            print("y か n を入力してください．")
            continue
        elif stdin == "y":
            return True
        else:
            return False


def loop_game(dataset: list) -> None:
    pass


def question_picker(src: list[list]) -> list[str]:
    pass


while 0:
    question = choice(cwr)
    reading = question[1]
    stdin = input(f"{question[0]} の読みは何でしょうか？ひらがなで答えてください．")
    if stdin == reading:
        print(f"正解！")
        cwr.remove(question)
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
