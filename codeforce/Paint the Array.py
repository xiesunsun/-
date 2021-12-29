# find a numebr d make adjacent number in arry divided d's result are different
import sys
import math
def input():
    return sys.stdin.readline().strip()
def judge(num):
    d=num[0]
    for i in num[::2]:
       d=math.gcd(d,i)
    if all([(i%d) for i in num[1::2]]):
        print(d)
        return
    d=num[1]
    for i in num[1::2]:
       d=math.gcd(d,i)
    if all([(i%d) for i in num[::2]]):
        print(d)
        return
    print(0)  
if __name__=='__main__':
    for _ in range(int(input())):
        input()
        judge(list(map(int,input().split())))