class Phonemes:
    """aka PhoneticInventory"""
    def __init__(self, consonants, vowels):
        self.consonants = consonants
        self.vowels = vowels


class Syllable:
    """aka PhoneticArray"""
    def __init__(self, phonemes, condition):
        self.phonemes = phonemes
        self.condition = condition

    def generate_simple_array(self) -> str:
        from random import choice
        return choice(self.phonemes.consonants) + choice(
            self.phonemes.vowels) + choice(self.phonemes.consonants)

    def generate_complex_array(self) -> str:
        onset = EqUtils.strsample(EqUtils, self.phonemes.consonants,
                                  self.condition["ccluster_size"])
        necleus = EqUtils.strsample(EqUtils, self.phonemes.vowels,
                                    self.condition["vcluster_size"])
        coda = EqUtils.strsample(EqUtils, self.phonemes.consonants,
                                 self.condition["ccluster_size"])
        return onset + necleus + coda


class EqUtils:
    def strsample(self, p, b: int) -> str:
        assert type(b) == int
        from random import randint as rint
        from random import sample
        p = list(p)
        return "".join(sample(p, (rint(1, b)))[:])

    def cherrypick(self, cond, src: dict) -> list:
        assert type(src) == dict
        cond = set(cond)
        return [k for k in src if cond <= src[k]]
