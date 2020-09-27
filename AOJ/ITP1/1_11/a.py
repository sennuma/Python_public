src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_11_A"


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

    @staticmethod
    def visiblefaces(self, f1, f2):
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


if __name__ == "__main__":
    d = Die(input().split())
    commands = input()
    for command in commands:
        d.rotate(command)
    print(d.faces["top"])
