# TLE 2206 ms
s = input()
b = len(s)
c = 0
f = 0
while True:
    if f == b:
        break
    elif b - f <= 2:
        f = 0
        b -= 1
    else:
        if int(s[f:b]) % 2019 == 0:
            c += 1
            f += 1
        else:
            f += 1
print(c)
