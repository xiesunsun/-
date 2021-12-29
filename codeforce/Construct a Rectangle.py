#judge whether can be consturcted a rectangle
import sys
def input():
    return sys.stdin.readline().strip()
def judgerec(num):
    fg=sum(num)%2
    jf2=sum(sorted(num,reverse=True)[1:])
    if fg==0:
        mnum=max(num)
        # res=[num.count(i) for i in set(num)]
        # 可以这样写存在相同的元素，那么元素之间一定有消耗的，set之后只要小于原来已知的长度就行
        if mnum!=jf2 and all(i<2 for i in num):
            print('NO')
        else:
            print('YES')            
    else:
        print('NO')
if __name__=='__main__':
    for _ in range(int(input())):
        judgerec(list(map(int,input().split())))
        