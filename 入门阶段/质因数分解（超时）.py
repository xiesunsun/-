#对于一个正整数n=a*b a、b都是质数，试求出二者中较大的那个质数
def judgeprim(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,round(num**(1/2))+1):
            if num%i==0:
                return False
        return True
def getprim(index):
    cont=0
    number=0;
    while(cont!=index):
        number+=1
        if judgeprim(number):
            cont+=1
    return number
#从小往大去找
if __name__=='__main__':
    n=eval(input())
    con=1
    while 1:
        num=getprim(con)
        if n%num==0 and judgeprim(n/num):
            print(round(n/num))
            break
        con+=1
            
             

