params = dict(obstrunt_coda=True,
              head_left=True,
              null_subject=True,
              null_onset=True,
              NP_left=False,
              consonant_cluster=False)

vowels = {
    "a": {"unrounded", "open", "back"},
    "i": {"unrounded", "close", "front"},
    "u": {"rounded", "close", "back"},
    "e": {"unrounded", "mid", "front"},
    "o": {"rounded", "mid", "back"},
}

consonants = {
    "k": {"voiceless", "velar", "plosive"},
    "g": {"voiced", "velar", "plosive"},
    "s": {"voiceless", "dental", "fricative"},
    "z": {"voiced", "dental", "fricative"},
    "t": {"voiceless", "dental", "plosive"},
    "d": {"voiced", "dental", "plosive"},
    "n": {"voiced", "dental", "nasal"},
    "h": {"voiceless", "glottal", "fricative"},
    "p": {"voiceless", "bilabial", "plosive"},
    "b": {"voiced", "bilabial", "plosive"},
    "m": {"voiced", "bilabial", "nasal"},
    "y": {"voiced", "palatal", "approximant"},
    "r": {"voiced", "alveolar", "tap"},
    "w": {"voiced", "bilabial", "approximant"},
    "": {None}
}

obstrunt = {"plosive", "fricative"}


def dict_to_cherrypicked_list(src: dict, cond: set) -> list:
    pass


def dict_to_cherrypicked_set(cond: set, src: dict) -> set:
    assert type(src) == dict, "src should be a dictionary"
    cond = set(cond)
    return {k for k in src if cond <= src[k]}


def gen_phon_arr(consonants, vowels) -> str:
    from random import choice
    consonants = list(consonants)
    vowels = list(vowels)
    return choice(consonants) + choice(vowels) + choice(consonants)
