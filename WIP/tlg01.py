class Consonants:
    def __init__(self, consonants: dict):
        self.d = consonants

    def save(self, destination):
        import json

        pass

    def load(self, destination):
        import json

        pass

    def search(self, conditions: set) -> list:
        return []

    def pickrandom(self, num=1) -> str:
        from random import choice

        return str([])


def pickrandom(d, n) -> str:
    from random import choices

    return "".join(choices(d, k=n))


consonants = {
    "p": ["voiceless", "bilabial", "stop"],
    "f": ["voiceless", "labiodental", "fricative"],
    "t": ["voiceless", "dental", "plosive"],
    "s": ["voiceless", "dental", "fricative"],
    "h": ["voiceless", "glottal", "fricative"],
    "w": ["voiced", "bilabial", "approximant"],
    "m": ["voiced", "bilabial", "nasal"],
    "b": ["voiced", "bilabial", "plosive"],
    "n": ["voiced", "dental", "nasal"],
    "d": ["voiced", "dental", "plosive"],
    "j": ["voiced", "palatal", "approximant"],
    "g": ["voiced", "velar", "plosive"],
}

vowels = {
    "a": ["open", "central", "unrounded"],
    "i": ["close", "front", "unrounded"],
    "u": ["close", "back", "rounded"],
}
