src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_9_D"

s = input()
for i in range(int(input())):
    command, *args = input().split()
    if command == "print":
        f, t = int(args[0]), int(args[1]) + 1
        print(s[f:t])
    elif command == "replace":
        f, t, r = int(args[0]), int(args[1]) + 1, args[2]
        s = s[:f] + r + s[t:]
    elif command == "reverse":
        f, t = int(args[0]), int(args[1]) + 1
        s = s[:f] + s[f:t][::-1] + s[t:]
