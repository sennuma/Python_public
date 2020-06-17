from random import choice, randint
import json


class Consonant:
    def __init__(self, consonant: dict):
        self.consonant = consonant.keys()
        self.place = None
        self.voice = None
        self.manner = None

    def save(self, destination):
        pass

    def load(self, destination):
        pass
