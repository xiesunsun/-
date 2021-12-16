n=eval(input())
data=list(map(int,input().split(' ')))
lenth=len(data)
step=0
for i in range(lenth):
    for j in range(i+1,lenth):
        if data[i]>data[j]:
            step+=1
            data[i],data[j]=data[j],data[i]
print(step)