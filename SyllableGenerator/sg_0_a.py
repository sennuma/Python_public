

class Consonant():
    poa_list = ["bilabial", "labiodental", "dental", "alveolar", "palatoalveolar",
                "retroflex", "alveopalatal", "palatal", "velar", "uvular", "pharyngeal", "glottal"]
    moa_list = ["nasal", "plosive", "fricative", "approximant", "tapflap",
                "trill", "lateralfricative", "lateralapproximant", "lateralflap"]

    def __init__(self, symbol: str, voiced: bool, poa: str, moa: str, **attr):
        assert type(symbol) == str
        assert type(voiced) == bool
        assert poa in Consonant.poa_list
        assert moa in Consonant.moa_list
        self.symbol = symbol
        self.poa = poa
        self.moa = moa
        self.voiced = voiced
        self.attr = attr


class Vowels():
    pass


class Phonotactics():
    pass


p = Consonant("p", False, "bilabial", "plosive")
b = Consonant("b", True, "bilabial", "plosive")
t = Consonant("t", False, "dental", "plosive")
d = Consonant("d", True, "dental", "plosive")
k = Consonant("k", False, "velar", "plosive")
g = Consonant("g", True, "velar", "plosive")
