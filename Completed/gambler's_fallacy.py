def gacha(n: int) -> float:
    """returns the possibility for getting a desired result which occurs once in nth try"""
    return 1-((n-1)/n)**n
