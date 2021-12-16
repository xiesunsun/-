#利用他们的思想不用那么多判断或者数据简单就好
a,b=map(int,input().split(' '))
data=[1 for x in range(a+1)]
for i in range(b):
    x,y=map(int,input().split(' '))
    for m in range(x,y+1):
        if m<a+1:
            data[m]=0
total=0
for i in data:
    if i==0:
        total+=1
print(a-total+1)
#101+99+
        

