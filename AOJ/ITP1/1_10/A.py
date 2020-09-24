# src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_A"

x1, y1, x2, y2 = map(float, input().split())
x, y = (x2 - x1) ** 2, (y2 - y1) ** 2
z = (x + y) ** 0.5
print(z)
