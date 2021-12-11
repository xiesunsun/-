a=list(map(int,input().split(' ')))
b=eval(input())+30
cot=0
for i in a:
    if b>=i:
        cot+=1
print(cot)