for _ in range(int(input())):
    n = int(input())
    data = list(map(int, input().split(' ')))
    flag = [False]*(n+1)  # 初始化是否被判断的标志,后面数据的下标索引是非零的
    arr = []  # 待处理数据
    for i in data:  # 这里注意一定要给指定位置的赋值，这里贪心的过程就是不做更改，用最小的step来实现
        if i <= n and not flag[i]:
            flag[i] = True
        else:
            arr.append(i)
    arr.sort()
    j = 0  # 从第一个待处理的变量开始处理，因为最小的替换位置是最小的
    for i in range(1, n+1):
        if not flag[i]:
            if arr[j] < (2*i+1):  # 右边的表达式代表余数范围有1-i的最小的数，可以算出了这个表达式，利用数学归纳法好想一点
                j = -1
                break
            j += 1  # 处理了一个（operation number）
    print(j)
