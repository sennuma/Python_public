def main():
    h, w = map(int, input().split())
    if h == w == 0:
        print()

    def lid(l):
        return "#" * l + "\n"

    def wall(l):
        return "#" + "." * (l - 2) + "#\n"

    def buildframe(size: tuple) -> str:
        frame = ""
        for i in range(size[0]):
            if i == 0 or i == size[0] - 1:
                frame += lid(size[1])
            else:
                frame += wall(size[1])
        print(frame)

    buildframe((h, w))


if __name__ == "__main__":
    main()
