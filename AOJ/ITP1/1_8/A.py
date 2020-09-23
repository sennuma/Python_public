# src = https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_A

from string import ascii_lowercase
from string import ascii_uppercase

ltc = dict(zip(ascii_lowercase, ascii_uppercase))
ctl = dict(zip(ascii_uppercase, ascii_lowercase))

stdin = input()
r = ""

for s in stdin:
    if s in ctl:
        r += ctl[s]
    elif s in ltc:
        r += ltc[s]
    else:
        r += s

print(r)
