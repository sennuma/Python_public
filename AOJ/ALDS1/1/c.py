src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_C"


def isprime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i <= x ** 0.5:
        if x % i == 0:
            return False
        i = i + 2
    return True


# ---- process ----
cnt = 0
n = int(input())
for i in range(n):
    if isprime(int(input())):
        cnt += 1
print(cnt)
