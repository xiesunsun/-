import sys
import copy
def input():
    return sys.stdin.readline().strip()
def judge(vertex):
    global resrd,rescd
    if vertex[0]==resrd or vertex[1]==rescd:
        return True
    else:
        return False
def move(vertex,flag1,flag2):
    vertex[0]+=flag1
    vertex[1]+=flag2
    return vertex
def truemove(vertex,flag1,flag2):
    vertex1=copy.deepcopy(vertex)
    result=hit(vertex1,flag1,flag2)
    if result[0]==1:
        flag1=-1
    if result[1]==1:
        flag2=-1
    vertex[0]+=flag1
    vertex[1]+=flag2
    return vertex,flag1,flag2
def hit(vertex,flag1,flag2):
    global rd,cd
    #r sitation
    move(vertex,flag1,flag2)
    res=[0,0]
    if vertex[0]<1 or vertex[0]>rd:
        res[0]=1
    if vertex[1]<1 or vertex[1]>cd:
        res[1]=1
    return res
if  __name__=='__main__':
    for _ in range(int(input())):
        data=list(map(int,input().split()))
        rd=data[0]
        cd=data[1]
        resrd=data[4]
        rescd=data[5]
        vertex=[data[1],data[2]]
        sum=0
        start=[data[2],data[3]]
        flag1=1
        flag2=1
        while not judge(start):
            rs=truemove(start,flag1,flag2)
            start=rs[0]
            flag1=rs[1]
            flag2=rs[2]
            sum+=1
        print(sum)