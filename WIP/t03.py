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
}

obstrunt = {"plosive", "fricative"}


def create_set_from_dict(condition: set, sourcedict: dict) -> set:
    assert type(sourcedict) == dict, "sourcedict should be a dictionary"
    condition = set(condition)
    return {k for k in sourcedict if condition <= sourcedict[k]}


# def naive_generate_phonetic_array(vowels: dict, consonants: dict,
#                                   params: dict) -> str:
#     assert type(vowels) == dict
#     assert type(consonants) == dict
#     assert type(params) == dict

#     # variables
#     vowels = create_set_from_dict({}, vowels)
#     consonants = create_set_from_dict({}, consonants)
#     if "null_onset" in params:
#         consonants.add("")
#     array = list()

#     from random import sample
#     array.append(str(sample(consonants, 1)))
#     array.append(str(sample(vowels, 1)))
#     array.append(str(sample(consonants, 1)))
#     return "".join(array)
