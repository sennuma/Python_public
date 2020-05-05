def main():
    w, h, x, y, r = (int(e) for e in input().split())
    # 円が (0, 0) からはみ出ているか
    if x - r < 0 or y - r < 0:
        print("No")
    # 円が (w, h) からはみ出ているか
    elif x + r > w or y + r > h:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
