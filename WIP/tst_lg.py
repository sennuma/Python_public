consonants = {
    "p": "voiceless, bilabial, plosive",
    "t": "voiceless, dental, plosive",
    "k": "voiceless, velar, plosive",
    "h": "voiceless, glottal, fricative",
    "y": "voiced, palatal, approximant",
    "w": "voiced, bilabial, approximant"
}
vowels = {
    "a": "open, centeral, unrounded",
    "i": "close, front, unrounded",
    "u": "close, back, rounded"
}


class Consonants:
    def __init__(self, consonants: dict) -> object:
        self.consonants = list(consonants.keys())


class Vowels:
    def __init__(self, parameter_list):
        raise NotImplementedError
