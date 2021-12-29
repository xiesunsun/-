#find square string just like abab
import sys
def input():
    return sys.stdin.readline().strip()
def judgestring(s):
    l=len(s)
    if l%2!=0:
        return False
    else:
        mid=l//2
        if s[0:mid]==s[mid:]:
            return True
    return False
if __name__=='__main__':
    for _ in range(int(input())):
        if(judgestring(input())):
            print('YES')
        else:
            print('NO')