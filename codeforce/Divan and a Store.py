#how to buy maximum chocolate 
import sys 
def input():
    return sys.stdin.readline().strip()
def calcu(num,l,r,k):
    countnum=0
    for i in sorted([i for i in num if l<=i<=r ]):
        if i<=k:
            countnum+=1
            k-=i
        else:
            break
    return countnum
if __name__=='__main__':
    for _ in range(int(input())):
           l,r,k=map(int,input().split()[1:])
           num=list(map(int,input().split()))
           print(calcu(num,l,r,k))
