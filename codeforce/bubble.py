# 冒泡排序
from sys import stdin


def input():
    return stdin.readline().strip()


data = list(map(int, input().split()))
for i in range(len(data)):  # control times of iteration
    # becasuse of adjacent elements compare will increment itself proposingly
    for j in range(0, len(data)-i-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]


print(" ".join((list(map(str, data)))))
