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
        self.zo = "NNNRNNNRNNNRNNNENNNRNNN"
        # 全探索用

    def __str__(self):
        return str(self.faces)

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
d = Die(input().split())
nq = int(input())
r = []
for i in range(nq):
    to, fr = tuple(map(int, input().split()))
    pass

for i in r:
    print(i)
