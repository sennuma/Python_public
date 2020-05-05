# inputの処理
# タプル内包表記 vs map
# 結果: ほとんど変化なし
import time


def main():
    x, y, z = (int(e) for e in "16 16 16".split())
    print(x, y, z)


def main2():
    x, y, z = map(int, "16 16 16".split())
    print(x, y, z)


if __name__ == "__main__":
    t1 = time.time()

    main()

    t2 = time.time()
    elapsed_time = t2 - t1
    print(f"elapsed time: {elapsed_time}")
