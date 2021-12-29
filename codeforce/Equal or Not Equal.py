#given a condition to prove whether have such a array
from sys import stdin
for _ in range(int(stdin.readline())):
    s=stdin.readline()
    if s.count('N')==1:
        print('NO')
    else:
        print('YES')
    