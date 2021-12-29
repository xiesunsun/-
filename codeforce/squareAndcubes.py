import sys
import math
reference=[]
def input():
    return sys.stdin.readline().strip()
def init():
    for i in range(1,1025):
        if round((i**3)**(1/2))==(i**3)**(1/2):
            reference.append(i**3)
def calcu(num):
    t1=math.floor(num**(1/2))
    t2=math.floor(num**(1/3))
    if (t2+1)**3==num:
        t2+=1
    sum=0
    for i,j in enumerate(reference):
        if num<j:
            sum=i
            break
    return t1+t2-sum 
if __name__=='__main__':
    init()
    for _ in range(int(input())):
        print(calcu(int(input())))