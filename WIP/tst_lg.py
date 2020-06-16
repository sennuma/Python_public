from random import choice, randint

consonants = {
    "p": ["voiceless", "bilabial", "stop"],
    "f": ["voiceless", "labiodental", "fricative"],
    "t": ["voiceless", "dental", "plosive"],
    "s": ["voiceless", "dental", "fricative"],
    "h": ["voiceless", "glottal", "fricative"],
    "w": ["voiced", "bilabial", "approximant"],
    "m": ["voiced", "bilabial", "nasal"],
    "n": ["voiced", "dental", "nasal"],
    "j": ["voiced", "palatal", "approximant"],
}

vowels = {
    "a": ["open", "central", "unrounded"],
    "i": ["close", "front", "unrounded"],
    "u": ["close", "back", "rounded"],
}


class WordGenerator:
    def __init__(self, consonants: dict, vowels: dict):
        self.consonants = consonants
        self.vowels = vowels

    def pickmatched(self, condition):
        def src(src):
            return [k for k in src if condition in src[k]]

        return src

    def genwords(self, num):
        result = []
        for i in range(num):
            result.append(
                choice(list(self.consonants.keys())) + choice(list(self.vowels.keys()))
            )
        return result
