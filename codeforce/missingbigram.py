import sys
def input():
    return sys.stdin.readline().strip()
def CaculatingString(num,l):
    res=[]
    res.append(num[0])
    for i in range(len(num)-1):
            if num[i][-1]==num[i+1][0]:
                res.append(num[i+1][-1])
            else:
                res.append(num[i+1])
    s="".join(res)
    if len(s)!=l:
        return s+'a'
    return s
if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        print(CaculatingString(input().split(),n))