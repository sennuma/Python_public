# src = https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_9_C

n = int(input())
tp, hp = 0, 0

for i in range(n):
    words = input().split()
    tw, hw = words[0], words[1]
    if tw == hw:
        tp += 1
        hp += 1
    elif tw > hw:
        tp += 3
    else:
        hp += 3

print(tp, hp)
