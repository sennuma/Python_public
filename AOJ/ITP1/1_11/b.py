src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_11_B"


class Die:
    def __init__(self, faces: list):
        self.faces = dict(
            top=faces[0],
            front=faces[1],
            right=faces[2],
            left=faces[3],
            back=faces[4],
            bottom=faces[5],
        )

    def __str__(self):
        return str(self.faces)

    def tofrri(self, to, fr):
        ri = 0
        for _ in range(2):
            for _ in range(3):
                for _ in range(4):
                    if self.issametopfro(to, fr):
                        ri = self.faces["right"]
                    self.rotate("R")
                self.rotate("N")
            self.rotate("R")
            self.rotate("S")
        return ri

    def issametopfro(self, tp, fr):
        if tp == self.faces["top"] and fr == self.faces["front"]:
            return True

    def rotate(self, direction):
        if direction == "S":
            (
                self.faces["top"],
                self.faces["front"],
                self.faces["bottom"],
                self.faces["back"],
            ) = (
                self.faces["front"],
                self.faces["bottom"],
                self.faces["back"],
                self.faces["top"],
            )
        elif direction == "N":
            (
                self.faces["top"],
                self.faces["back"],
                self.faces["bottom"],
                self.faces["front"],
            ) = (
                self.faces["back"],
                self.faces["bottom"],
                self.faces["front"],
                self.faces["top"],
            )
        elif direction == "E":
            (
                self.faces["top"],
                self.faces["left"],
                self.faces["bottom"],
                self.faces["right"],
            ) = (
                self.faces["left"],
                self.faces["bottom"],
                self.faces["right"],
                self.faces["top"],
            )
        elif direction == "W":
            (
                self.faces["top"],
                self.faces["right"],
                self.faces["bottom"],
                self.faces["left"],
            ) = (
                self.faces["right"],
                self.faces["bottom"],
                self.faces["left"],
                self.faces["top"],
            )
        elif direction == "R":
            (
                self.faces["front"],
                self.faces["right"],
                self.faces["back"],
                self.faces["left"],
            ) = (
                self.faces["right"],
                self.faces["back"],
                self.faces["left"],
                self.faces["back"],
            )
        elif direction == "L":
            (
                self.faces["front"],
                self.faces["left"],
                self.faces["back"],
                self.faces["right"],
            ) = (
                self.faces["left"],
                self.faces["back"],
                self.faces["right"],
                self.faces["front"],
            )


# main
d = Die([1, 2, 3, 4, 5, 6])
