# find satisfiction pairwise number
import sys
def input():
    return sys.stdin.readline().strip()
def getpair(num,limit):
    data=sorted(num,reverse=True)
    res=[]
    sum=0
    for i in range(len(data)-1):
        for j in range(i+1,len(data)):
            if (data[i] % data[-j]) not in data[-j:]:
                res.append([data[i],data[j]])
                sum+=1 
            if sum==limit:
                return res
    return 'what happeded??????'
def getpair2(num,limit):
    data=sorted(num,reverse=True)
    for i in range(limit):
        print(f'{data[i]} {data[-1]}')
if __name__=='__main__':
    #  print(getpair(list(map(int,input().split()))))
    # print(getpair([2,8,3,4],2))
    for _ in range(int(input())):
        lm=int(input())//2
        getpair2(list(map(int,input().split())),lm)