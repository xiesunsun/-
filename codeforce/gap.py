import sys
def input():
    return sys.stdin.readline().strip()
for _ in range(int(input())):
    n=int(input())
    data=list(map(int,input().split()))
    if sum(data)/n==round(sum(data)/n):#这一步就是判断能否整除只要%就可以，但是这个也可以用来判断一个数是否是小数
        print(0)
    else:
        print(1)

    