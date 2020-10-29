import json
from urllib import parse

import requests as req


class Geoapi:
    """
    Fetching data via GeoAPI and its manipulation.

    dataset: list[tuple] -> pass
    """

    def __init__(self, prefecture):
        """
        prefecute: str -> give it as kanji.

        If the prefecture has ever been fetched, get the data from the local storage.
        Otherwise, fetch the information via the API and dump it to local storage.

        """
        if hasfetched(prefecture):
            with open(".\\json\\{}.json".format(prefecture), encoding="utf8") as f:
                self.json = json.load(f)

        else:
            self.response: req.Request = req.get(
                "http://geoapi.heartrails.com/api/json?method=getCities&prefecture="
                + parse.quote(prefecture)
            )
            self.json: dict = self.response.json()

            with open(
                ".\\json\\{}.json".format(prefecture), mode="w", encoding="utf8"
            ) as f:
                json.dump(self.json, f, indent=2, ensure_ascii=False)

            with open(".\\json\\fetched.json", encoding="utf8") as f:
                d: dict = json.load(f)
                d["fetched"].append(prefecture)
            with open(".\\json\\fetched.json", mode="w", encoding="utf8") as f:
                json.dump(d, f, indent=2, ensure_ascii=False)

        self.contents: list = self.json["response"]["location"]
        self.dataset: list[tuple] = [(i["city"], i["city_kana"]) for i in self.contents]


def fetch_pref_data(prefecture):
    """
    fetch prefecture data with ease.
    """
    with open(".\\json\\{}.json".format(prefecture), encoding="utf8") as f:
        d = json.load(f)
    return d


def hasfetched(prefecture) -> bool:
    """
    check if the prefecture has been fetched already.
    """
    with open(".\\json\\fetched.json", encoding="utf8") as f:
        d = json.load(f)
    if prefecture in d["fetched"]:
        return True
    return False
