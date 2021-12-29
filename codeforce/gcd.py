def ogcd(a,b):
    if a<b:
        a,b=b,a
    while(b!=0):
        tmp=b
        a,b=b,a%b
    if tmp==1:
        return True
    return False
def test(n):
    for i in range(2,n//2):
            if ogcd(i,n-1-i):
                print(f'{i} {n-1-i} 1')
                return
for i in range(int(input())):
        test(int(input()))
