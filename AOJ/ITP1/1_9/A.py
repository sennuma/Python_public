# src = https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_9_A

from string import punctuation as punc

table = {i: None for i in punc}

w = input().upper()
text = []

while 1:
    line = input()
    if line == "END_OF_TEXT":
        break
    line = line.upper().translate(str.maketrans(table))
    text += line.split(" ")

print(text.count(w))
