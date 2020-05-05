# src = https://img.atcoder.jp/abc164/editorial.pdf
# prob = https://atcoder.jp/contests/abc164/tasks/abc164_d
# しんだ。

# 変数
#s = input()
s = "1817181712114"
n = len(s)


def t(k: int, s: str):
    return int(s[k:])


# (i, j)が条件を満たすのは t(i, s) == t(j, s) % 2019
# 各t(i, s) % 2019 を計算し、modの値が同じ事の個数を計算して
# 足したものが答え。
cnt = 0
for i in range(n):
    for j in range(n):
        if i <= j:
            if t(i, s) == t(j, s) % 2019:
                cnt += 1
        else:
            continue

# デバッグ
print("s =", s)
print("tk(k=0, s) =", str(t(0, s)))
print("cnt = ", str(cnt))

# 出力
pass
