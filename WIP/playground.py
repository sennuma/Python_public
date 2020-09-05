from t04 import Phonemes
from t04 import Syllable
from t04 import Phonetic_array_generator

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
    "f": {"voiceless", "labiodental", "fricative"},
    "v": {"voiced", "labiodental", "fricative"},
    "n": {"voiced", "dental", "nasal"},
    "h": {"voiceless", "glottal", "fricative"},
    "p": {"voiceless", "bilabial", "plosive"},
    "b": {"voiced", "bilabial", "plosive"},
    "m": {"voiced", "bilabial", "nasal"},
    "j": {"voiced", "palatal", "approximant"},
    "r": {"voiced", "alveolar", "tap"},
    "R": {"voiced", "alveolar", "trill"},
    "w": {"voiced", "bilabial", "approximant"},
    "": {None}
}

params = {
    "obstrunt_coda": True,
    "head_initial": True,
    "null_onset": True,
    "NP_initial": True,
    "ccluster_size": 2,
    "vcluster_size": 2,
}

phonemes = Phonemes(consonants, vowels)
syllable = Syllable(phonemes, params)
gentor = Phonetic_array_generator(syllable)
