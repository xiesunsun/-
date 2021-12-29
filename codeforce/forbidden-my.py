res=[]
S=[]
T=[]
# 我其实没必要循环一次，判断一次的，我大可以直接在输入的时候进行判断的操作
for i in range(eval(input())):
    S.append(list(input())) 
    T.append(input())
for i in range(len(S)):
    tmpl=S[i]
    tmpl.sort()
    tmp=list(set(tmpl))
    tmp.sort(key=tmpl.index)
    if(T[i] in "".join(tmp)):
        m=tmpl.index('b')
        n=tmpl.index('c')
        for j in range(tmpl.count('c')):
            tmpl[m+j],tmpl[n+j]=tmpl[n+j],tmpl[m+j]
        res.append(tmpl)   
    else:
        res.append(tmpl)
for i in res:
    print("".join(i))
    

    
    
