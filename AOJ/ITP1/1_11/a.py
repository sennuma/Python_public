class Die:
    def __init__(self, faces: list):
        self.top = faces[0]
        self.front = faces[1]
        self.right = faces[2]
        self.left = faces[3]
        self.back = faces[4]
        self.bottom = faces[5]

    def rotate(self, direction):
        if direction == "S":
            self.top, self.back, self.bottom, self.front = (
                self.back,
                self.bottom,
                self.front,
                self.top,
            )
        elif direction == "N":
            self.top, self.front, self.bottom, self.back = (
                self.front,
                self.bottom,
                self.back,
                self.top,
            )
        elif direction == "E":
            self.top, self.left, self.bottom, self.right = (
                self.left,
                self.bottom,
                self.right,
                self.top,
            )
        else:  # direction == "W"
            self.top, self.right, self.bottom, self.left = (
                self.right,
                self.bottom,
                self.left,
                self.top,
            )


if __name__ == "__main__":
    d = Die(input().split())
    commands = input()
    for command in commands:
        d.rotate(command)
    print(d.top)
