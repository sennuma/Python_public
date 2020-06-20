lang1_path = r".\\lang1\\lang1.json"


def save(dest: str, dictionary: dict):
    """facilitates dumping Python dict into json"""
    import json
    with open(dest, "w") as f:
        json.dump(dictionary, f, indent=4)


def load(path: str) -> dict:
    """facilitates loading json into Python dict"""
    import json
    with open(path, "r") as f:
        return json.load(f)


def pick_conditioned(s: dict, c: set, n: int) -> str:
    """returns n sized string under the given condition (c) from s."""
    from random import choice
    result = []
    for _ in range(n):
        result.append(choice([x for x in s if c < set(s[x])]))
    return "".join(result)


def pick_random(seq, n=1) -> str:
    from random import choices
    try:
        seq = list(seq)
    except TypeError as e:
        print(e)

    return "".join(choices(seq, k=n))


phonemes = load(lang1_path)
consonants = phonemes["consonants"]
vowels = phonemes["vowels"]
