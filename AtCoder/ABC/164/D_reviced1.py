# 参考 = https://qiita.com/Seika139/items/8cacdb3cc8fa6655573c
# 問題 = https://atcoder.jp/contests/abc164/tasks/abc164_d


def main():
    # S = input()[::-1]  # 入力を逆順に入れ替え
    S = "1817181712114"
    ans = 0
    mods = [0] * 2019
    mods[0] = 1
    current = 0
    x = 1
    for s in S:
        current = (current + x * int(s)) % 2019
        ans += mods[current % 2019]
        mods[current % 2019] += 1
        x = x * 10 % 2019
    print(ans)


if __name__ == "__main__":
    main()
