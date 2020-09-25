# src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_B"

from math import radians
from math import sin
from math import cos

a, b, c = map(float, input().split())
c = radians(c)

s = 0.5 * a * b * sin(c)
_ = a ** 2 + b ** 2 - 2 * a * b * cos(c)
_ = _ ** 0.5
l = a + b + _
h = 2 * s / a

for i in (s, l, h):
    print("{:.6f}".format(i))
