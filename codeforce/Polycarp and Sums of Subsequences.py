import sys
def input():
    return sys.stdin.readline().strip()
def getarry(num):
    z=num[-2]+num[-3]-num[-1]
    x=num[-1]-num[-2]
    y=num[-1]-num[-3]
    return [x,y,z]
if __name__=='__main__':
    for _ in range(int(input())):
        num=list(map(int,input().split()))
        res=getarry(num)
        print(res[0],res[1],res[2])