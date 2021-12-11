#同项为1/n的级数的求和使之大于给定数值k
#输入k，返回满足条件的最小K
n=eval(input())
sum=0
cot=0
while sum<=n:
    cot+=1
    sum+=1/cot
print(cot)