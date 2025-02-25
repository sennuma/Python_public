class Phonemes:
    """aka PhoneticInventory"""

    def __init__(self, consonants, vowels):
        self.consonants = consonants
        self.vowels = vowels


class Syllable:
    def __init__(self, phonemes, conditions):
        self.phonemes = phonemes
        self.conditions = conditions


class Phonetic_array_generator:
    def __init__(self, syllable):
        assert isinstance(syllable, Syllable)
        self.consonants = syllable.phonemes.consonants
        self.vowels = syllable.phonemes.vowels
        self.conditions = syllable.conditions

    def gen_naive_single(self):
        from random import choice

        onset = choice(list(self.consonants))
        necleus = choice(list(self.vowels))
        coda = choice(list(self.consonants))
        return onset + necleus + coda

    def gen_naive_multiple(self):
        onset = EqUtils.strsample(self.consonants, self.conditions["ccluster_size"])
        necleus = EqUtils.strsample(self.vowels, self.conditions["vcluster_size"])
        coda = EqUtils.strsample(self.consonants, self.conditions["ccluster_size"])
        return onset + necleus + coda
        # 日r本o語eは+２eバeイ トc文a字


class EqUtils:
    @staticmethod
    def strsample(p, b: int) -> str:
        assert type(b) == int
        from random import randint as rint
        from random import sample

        p = list(p)
        return "".join(sample(p, (rint(1, b)))[:])

    @staticmethod
    def cherrypick(cond, src: dict) -> list:
        assert type(src) == dict
        cond = set(cond)
        return [k for k in src if cond <= src[k]]
