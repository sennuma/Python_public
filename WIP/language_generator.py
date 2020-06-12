def main():
    class Language:
        pass

    class Word:
        pass

    class Phonotactics:
        pass

    class Consonants:
        pass

    class Vowels:
        pass

    class Consonant:
        def __init__(
            self, grapheme: str, voiced: bool, place: str, manner: str, **kwargs
        ) -> object:
            self.grapheme = str(grapheme)
            self.voiced = voiced
            self.place = place.title()
            self.manner = manner.title()
            try:
                self.attributes = kwargs
            except NameError:
                self.attributes = None

    class Vowel:
        def __init__(
            self, grapheme: str, height: str, backness: str, roundness: bool, **kwargs
        ) -> object:
            self.grapheme = str(grapheme)
            self.height = height.title()
            self.backness = backness.title()
            self.roundness = roundness
            try:
                self.attributes = kwargs
            except NameError:
                self.attributes = None

    # a = Vowel("a", "open", "center", False, length="short")
    # i = Vowel("i", "close", "front", False, length="short")
    # u = Vowel("u", "close", "back", True, length="short")

    vowels = {
        "a": ["open", "center", False, "short"],
        "i": ["close", "front", False, "short"],
        "u": ["close", "back", True, "short"],
    }

    p = Consonant("p", False, "bilabial", "plosive")
    t = Consonant("t", False, "dental", "plosive")
    k = Consonant("k", False, "velar", "plosive")
    h = Consonant("h", False, "glottal", "fricative")
    w = Consonant("w", True, "bilabial", "approximant")
    y = Consonant("y", True, "palatal", "approximant")
    s = Consonant("s", False, "dental", "fricative")
    r = Consonant("r", True, "dental", "trill")
    l = Consonant("l", True, "dental", "lateral approximant")
    m = Consonant("m", True, "bilabial", "nasal")
    n = Consonant("n", True, "dental", "nasal")


if __name__ == "__main__":
    main()
