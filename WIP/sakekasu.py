"""module explanation
"""


def typechecker(arg, *types):
    if type(arg) not in set(types):
        raise ValueError(types)


class AlcBev:
    """
    Stores information for alcoholic beverage.

    Atrributes
    ----------
    name: str
        Name of the beverage.
    apv: int
        Alcohol per volume of the beverage.
    vol: int
        Volume of the beverage.
    price: int
        Price of the beverage.
    ppa: float
        Price per alcohol.
    app: float
        Alcohol per price.
    """

    def __init__(self, name: str, apv: int, vol: int, price: int):
        """
        Parameters
        ----------
        name: str
            The name of the beverage.
        apv: int
            Alcohol per volume. Should be given in 100 times of its percentage.
            i.e. if its apv is 9%, 9 should be given.
        vol: int
            Volume. Should be given in mL.
        price: int
            Price of the alcoholic beverage.
        """

        if type(name) not in {str}:
            raise TypeError(str)
        self.name = name

        if type(apv) not in {int}:
            raise TypeError(int)
        if apv >= 100:
            raise ValueError("Param apv should be less than 100.")
        self.apv = apv

        if type(vol) not in {int}:
            raise TypeError(int)
        if vol < 0:
            raise ValueError("Param vol should be more than 0.")
        self.vol = vol

        if type(price) not in {int}:
            raise TypeError(int)
        if price < 0:
            raise ValueError("Param price should be more than 0.")
        self.price = price

        self.ppa = price / apv
        self.app = apv / price


n = AlcBev("Nikka", 37, 180, 450)
