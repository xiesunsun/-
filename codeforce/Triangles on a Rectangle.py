import sys


def input():
    return sys.stdin.readline().strip()


for _ in range(int(input())):
    w,h=map(int,input().split())
    arry1 = list(map(int, input().split()))[1:]
    arry2 = list(map(int, input().split()))[1:]
    arry3 = list(map(int, input().split()))[1:]
    arry4 = list(map(int, input().split()))[1:]
    area1=(arry1[-1]-arry1[0])*h
    area2=(arry2[-1]-arry2[0])*h
    area3=(arry3[-1]-arry3[0])*w
    area4=(arry4[-1]-arry4[0])*w
    print(max(area1,area2,area3,area4))