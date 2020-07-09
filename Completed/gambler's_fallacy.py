def gacha(n: int) -> float:
    """returns a percentage of getting a desired outcome which happens once in nth tries."""
    return 1 - ((n - 1) / n) ** n
