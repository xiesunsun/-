#傻瓜的操作
n=eval(input())
for i in range(2,round(n**(1/2))+1):
    if n%i==0:
        print(round(n/i))
        break
    