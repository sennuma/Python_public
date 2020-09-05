params = dict(obstrunt_coda=True,
              head_initial=True,
              null_subject=True,
              null_onset=True,
              NP_initial=False,
              ccluster_size=2,
              vcluster_size=2)

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


def strised_sample(p, n_min: int, n_max: int) -> str:
    """a function based on random.sample and random.randint"""
    assert type(n_min) == int
    assert type(n_max) == int
    from random import randint as rint
    from random import sample
    p = list(p)

    return "".join(sample(p, rint(n_min, n_max))[:])


def gen_phon_arr01(c, v) -> str:
    """c for consonants, v for vowels.\n
    returns a string that consists of a random choice from given c and v."""
    from random import choice
    c = list(c)
    v = list(v)
    return choice(c) + choice(v) + choice(c)


def gen_phon_arr02(c, v, cond) -> str:
    """c, v, and cond stand for consonants, vowels and condition respectively.\n
    returns a string that consists of a random choices from given c and v.
    the number of choices from c or v depends on
    cond[ccluster_size] and cond[vcsluter_size] respectively."""

    c, v = list(c), list(v)

    csize, vsize = cond["ccluster_size"], cond["vcluster_size"]

    return strised_sample(c, 1, csize) + strised_sample(
        v, 1, vsize) + strised_sample(c, 1, csize)


def gen_phon_arr03(c, v, cond) -> dict:
    pass
