def main():
    class Language:
        pass

    class Word:
        pass

    class Phonotactics:
        pass

    class Consonants:
        def __init__(self, characters: dict) -> object:
            pass

    class Vowels:
        pass

    # class Consonant:
    #     def __init__(
    #         self, grapheme: str, voiced: bool, place: str, manner: str, **kwargs
    #     ) -> object:
    #         self.grapheme = str(grapheme)
    #         self.voiced = voiced
    #         self.place = place.title()
    #         self.manner = manner.title()
    #         try:
    #             self.attributes = kwargs
    #         except NameError:
    #             self.attributes = None

    # class Vowel:
    #     def __init__(
    #         self, grapheme: str, height: str, backness: str, roundness: bool, **kwargs
    #     ) -> object:
    #         self.grapheme = str(grapheme)
    #         self.height = height.title()
    #         self.backness = backness.title()
    #         self.roundness = roundness
    #         try:
    #             self.attributes = kwargs
    #         except NameError:
    #             self.attributes = None

    # a = Vowel("a", "open", "center", False, length="short")
    # i = Vowel("i", "close", "front", False, length="short")
    # u = Vowel("u", "close", "back", True, length="short")

    vowels = {
        "a": "open, central, unrounded, short",
        "i": "close, front, undounded, short",
        "u": "close, back, rounded, short"
    }

    consonants = {
        "p": "voiceless, bilabial, plosive",
        "t": "voiceless, dental, plosive",
        "k": "voiceless, velar, plosive",
        "h": "voiceless, glottal, fricative",
        "w": "voiced, bilabial, approximant",
        "y": "voiced, palatal, approximant"
    }


if __name__ == "__main__":
    main()
