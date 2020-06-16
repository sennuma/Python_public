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


class Consonants:
    def __init__(self, consonants: dict):
        self.consonants = list(consonants.keys())
        self.d = consonants
