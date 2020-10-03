class Die:
    def __init__(self, faces):
        """create an instance of a die."""
        self.faces = dict(
            tp=faces[0], ft=faces[1], rt=faces[2], lt=faces[3], bk=faces[4], bm=faces[5]
        )
        # tp=0, ft=1, rt=2, lt=3, bk=4, bm=5

    def __str__(self):
        return str(self.faces)

    def rotate(self, d):
        """rotate the die to the given direction."""
        if d not in "NEWSRL":
            raise ValueError
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

    def alles(self) -> tuple:
        """returns all possible states of the die as a tuple."""
        ords = "RRRERRRERRRWRRRWRRRERRR"
        r = []
        for o in ords:
            r.append(tuple(self.faces.values()))
            self.rotate(o)
        else:
            r.append(tuple(self.faces.values()))
        return tuple(r)

    def _rt(self, tp, ft) -> int:
        """returns the right face which appears when the given faces are visible."""
        alles = self.alles()
        for e in alles:
            if e[0] == tp and e[1] == ft:
                rt = e[2]
        return rt


d = Die(list(map(int, input().split())))
nq = int(input())
results = []
for _ in range(nq):
    tp, ft = tuple(map(int, input().split()))
    results.append(d._rt(tp, ft))

for result in results:
    print(result)
