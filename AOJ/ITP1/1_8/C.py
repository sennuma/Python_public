# src = https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_C

from string import ascii_lowercase
import sys

table = {i: 0 for i in ascii_lowercase}
strings = sys.stdin.read().lower()

for s in strings:
    if s in table:
        table[s] += 1

for i in table:
    print(f"{i} : {table[i]}", end="\n")
