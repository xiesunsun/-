# given arry scope find delete times
# print(int(bin(10)[2:]))
#此题超时暂时搞不懂啊
import sys
import math
value = [[0 for _ in range(20)] for _ in range(200001)]


def input():
    return sys.stdin.readline().strip()


def getvalue():
    for i in range(1, 200001):
        tmp = list(map(int, (bin(i)[2:])[::-1]))
        for m, n in enumerate(tmp):
            if n == 1:
                value[i][m] += 1


def main():
    for _ in range(int(input())):
        data = [0]*20
        l, r = map(int, input().split())
        for i in range(l, r+1):
                for m,j in enumerate(value[i]):
                    data[m]+=j 
        print(r-l+1-max(data))


if __name__ == '__main__':
    getvalue()
    main()
