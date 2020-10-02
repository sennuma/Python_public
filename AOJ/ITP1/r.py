class Die:
    def __init__(self, faces):
        self.faces = dict(
            tp=faces[0], ft=faces[1], rt=faces[2], lt=faces[3], bk=faces[4], bm=faces[5]
        )

    def __str__(self):
        return str(self.faces)

    def rotate(self, d):
        if d not in "NEWSRL":
            raise NotImplementedError
        elif d == "S":
            (
                self.faces["tp"],
                self.faces["bk"],
                self.faces["bm"],
                self.faces["ft"],
            ) = (
                self.faces["bk"],
                self.faces["bm"],
                self.faces["ft"],
                self.faces["tp"],
            )
        elif d == "N":
            (
                self.faces["tp"],
                self.faces["ft"],
                self.faces["bm"],
                self.faces["bk"],
            ) = (
                self.faces["ft"],
                self.faces["bm"],
                self.faces["bk"],
                self.faces["tp"],
            )
        elif d == "W":
            (
                self.faces["tp"],
                self.faces["rt"],
                self.faces["bm"],
                self.faces["lt"],
            ) = (
                self.faces["rt"],
                self.faces["bm"],
                self.faces["lt"],
                self.faces["tp"],
            )
        elif d == "E":
            (
                self.faces["tp"],
                self.faces["lt"],
                self.faces["bm"],
                self.faces["rt"],
            ) = (
                self.faces["lt"],
                self.faces["bm"],
                self.faces["rt"],
                self.faces["tp"],
            )
        elif d == "L":
            (
                self.faces["ft"],
                self.faces["rt"],
                self.faces["bk"],
                self.faces["lt"],
            ) = (
                self.faces["rt"],
                self.faces["bk"],
                self.faces["lt"],
                self.faces["ft"],
            )
        elif d == "R":
            (
                self.faces["ft"],
                self.faces["lt"],
                self.faces["bk"],
                self.faces["rt"],
            ) = (
                self.faces["lt"],
                self.faces["bk"],
                self.faces["rt"],
                self.faces["ft"],
            )

    def alles(self):
        ords = "RRRERRRERRRWRRRWRRRERRR"
        r = set()
        for o in ords:
            r.add(tuple(self.faces.values()))
            self.rotate(o)
            print(self.faces)
        else:
            r.add(tuple(self.faces.values()))
        return r


from pprint import pprint as p

d = Die([1, 2, 3, 4, 5, 6])

