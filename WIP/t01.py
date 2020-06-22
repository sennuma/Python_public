lang1_path = r".\\lang1\\lang1.json"
lang2_path = r".\\lang1\\lang2.json"


def save_direct(dest: str, dictionary: dict):
    """facilitates dumping Python dict into json"""
    import json

    with open(dest, "w") as f:
        json.dump(dictionary, f, indent=4)


def save_dictionary_with_set(dest: str, dictionary: dict):
    # WIP: not available if set is embeded outside of the initial values
    save_direct(dest, {k: list(dictionary[k]) for k in dictionary})


def save(destination: str, dictionary: dict, mode="d"):
    """mode:
        d -> directly dumps dictionary into json
        c -> convert values as set into them as list and dumps into json"""
    validmodes = {"d", "c"}
    import json
    assert set(mode) < validmodes


def load_direct(path: str) -> dict:
    """facilitates loading json into Python dict"""
    import json

    with open(path, "r") as f:
        return json.load(f)


def load_dictionary_values_as_set(path: str) -> dict:
    return {k: set(load_direct(path)[k]) for k in load_direct(path)}


def convert_values_to_set(d: dict):
    try:
        result = {k: set(d[k]) for k in d}
    except TypeError as e:
        raise e
    return result


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


phonemes = load_direct(lang1_path)
consonants = convert_values_to_set(phonemes["consonants"])
vowels = convert_values_to_set(phonemes["vowels"])
