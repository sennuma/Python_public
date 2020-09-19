input()  # 配列の長さの情報はいらないので捨てる
print(*input().split()[::-1])
# input()<type::str>をsplit()したやつ<type::list>を[::-1]で逆順にしてそれを*でアンパックしてprint関数に渡す．
