params = dict(obstrunt_coda=True,
              head_left=True,
              null_subject=True,
              null_onset=True,
              NP_left=False)

vowels = {
    "a": {"unrounded", "open", "back"},
    "i": {"unrounded", "close", "front"},
    "u": {"rounded", "close", "back"},
    "e": {"unrounded", "mid", "front"},
    "o": {"rounded", "mid", "back"},
}

# %%
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
}
# %%
obstrunt = {"plosive", "fricative"}


def create_set_from_dict(condition: set, sourcedict: dict) -> set:
    assert type(sourcedict) == dict, "sourcedict should be a dictionary"
    condition = set(condition)
    return {k for k in sourcedict if condition <= sourcedict[k]}


def generate_phonetic_array(vowels: dict, consonants: dict,
                            params: dict) -> list:
    assert type(vowels) == dict
    assert type(consonants) == dict
