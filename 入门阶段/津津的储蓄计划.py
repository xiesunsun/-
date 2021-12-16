#津津的一个策略是如果当月妈妈给的钱在月末（需要减去花销）后大于等于100，就放到妈妈那里去
sdata=[]
for i in range(12):
    sdata.append(eval(input()))
salary=0
total=salary
savings=0
#计算公式是什么
def calcu():
    global savings,total
    tmp=0
    for i,j in enumerate(sdata):
        tmp=total-j+300
        if tmp>=0:
            if tmp>=100:
                given=(tmp//100)*100
                savings+=given
                tmp=tmp-given
            total=tmp
        else:
            print(-(i+1))
            return
    print(round(savings*1.2+total))
calcu()

        