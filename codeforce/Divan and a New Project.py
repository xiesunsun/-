#Divan and a New Project
from operator import itemgetter
from sys import stdin
def input():
    return stdin.readline().strip()
def getcoordinate(num):
    #default coordinate for headquarters is 0
    power=dict(sorted(enumerate(num),key=itemgetter(1),reverse=True))
    sum=0
    countnum=0
    coordinate=1
    for i in power.items():
        sum+=coordinate*power[i[0]]
        power[i[0]]=((-1)**countnum)*coordinate
        countnum+=1
        if countnum%2==0:
            coordinate+=1
    print(sum*2)
    return power
if __name__=='__main__':
    for _ in range(int(input())):
        input()
        c=(list(sorted((getcoordinate(list(map(int,input().split())))).items(),key=itemgetter(0))))
        b=[0]
        b.extend([i[1] for i in c ])
        for i in b:
            print(i,end=' ')

