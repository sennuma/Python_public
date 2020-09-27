# src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_11_B"
run = 1


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

    def visiblefaces(self, f=-1, t=-1, r=-1) -> str:
        rev = {self.faces[k]: k for k in self.faces}
        if f == -1:
            for i in rev:
                if t == i:
                    self.align(rev[i], "top")
            for i in rev:
                if r == i:
                    self.align(rev[i], "right")
            return self.faces["front"]
        elif t == -1:
            for i in rev:
                if f == i:
                    self.align(rev[i], "front")
            for i in rev:
                if r == i:
                    self.align(rev[i], "right")
            return self.faces["top"]
        elif r == -1:
            for i in rev:
                if f == i:
                    self.align(rev[i], "front")
            for i in rev:
                if t == i:
                    self.align(rev[i], "top")
            return self.faces["right"]

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
        elif direction == "L":
            (
                self.faces["front"],
                self.faces["right"],
                self.faces["back"],
                self.faces["left"],
            ) = (
                self.faces["right"],
                self.faces["back"],
                self.faces["left"],
                self.faces["front"],
            )
        elif direction == "R":
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


if __name__ == "__main__" and run:
    from copy import copy

    results = []
    d = Die(faces=input().split())
    for i in range(int(input())):
        dd = copy(d)
        t, f = map(int, tuple(input().split()))
        results.append(dd.visiblefaces(t=t, f=f))
    for result in results:
        print(result)
