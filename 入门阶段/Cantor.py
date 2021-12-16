#1/1  1/2  1/3 1/4
#2/1  2/2  3/2 4/2
#3/1  3/2  3/3 3/4
#4/1  4/2  4/3 4/4
#第7个为 1+2+3 +1
def getlimit(n):
    cont=0
    sumnum=0
    while sumnum<n:
        cont+=1
        sumnum+=cont
    return (cont-1,n-(cont*(cont-1))/2)
a,b=getlimit(eval(input()))
if(a%2==0):
    print(f'{round(a+2-b)}/{round(b)}')
else:
    print(f'{round(b)}/{round(a+2-b)}')