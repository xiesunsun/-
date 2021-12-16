n=eval(input())
data=list(set(map(int,input().split(' '))))
(data).sort()
print(len(data))
for i in data:
    print(i,'',end='')