<<<<<<< Updated upstream
# src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_11_B"
run = 0
=======
src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_11_A"
dbg = 1
>>>>>>> Stashed changes


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
<<<<<<< Updated upstream

    def align(self, face, dest) -> None:
        if (face, dest) in list(
            zip(
                ["front", "top", "back", "bottom"],
                ["back", "bottom", "front", "top"],
            )
        ):
            self.rotate("N")
            self.rotate("N")
        elif (face, dest) in list(zip(["right", "left"], ["left", "right"])):
            self.rotate("R")
            self.rotate("R")
        elif (face, dest) in list(
            zip(["right", "back", "left", "front"], ["back", "left", "front", "right"])
        ):
            self.rotate("R")
        elif (face, dest) in list(
            zip(["right", "front", "left", "back"], ["front", "left", "back", "right"])
        ):
            self.rotate("L")
        elif (face, dest) in list(
            zip(["top", "front", "bottom", "back"], ["front", "bottom", "back", "top"])
        ):
            self.rotate("S")
        elif (face, dest) in list(
            zip(["top", "back", "bottom", "front"], ["back", "bottom", "front", "top"])
        ):
            self.rotate("N")
        elif (face, dest) in list(
            zip(["top", "right", "bottom", "left"], ["right", "top", "left", "bottom"])
        ):
            self.rotate("E")
        elif (face, dest) in list(
            zip(["top", "left", "bottom", "right"], ["left", "bottom", "right", "top"])
        ):
            self.rotate("W")
=======
>>>>>>> Stashed changes

    def mtd(self, t, f):
        if t == self.faces["top"]:
            pass
        elif t == self.faces["front"]:
            pass

    def rotate(self, direction):
        if direction == "S":
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
        elif direction == "N":
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
        else:  # direction == "W"
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


<<<<<<< Updated upstream
a = Die([1, 2, 3, 4, 5, 6])
p = print

if __name__ == "__main__" and run:
    from copy import copy
=======
if __name__ == "__main__" and not dbg:
    d = Die(input().split())
    commands = input()
    for command in commands:
        d.rotate(command)
    print(d.faces["top"])
>>>>>>> Stashed changes

if __name__ == "__main__" and dbg:
    d = Die([1, 2, 3, 4, 5, 6])
    p = print
