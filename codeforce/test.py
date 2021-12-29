def test(num):
    res = []
    for i in range(2, num+1):
        res.append(num % i)
    rs = list(set(res))
    rs.sort()
    rs.remove(0)
    return rs
def resolve(num):
    res = []
    for i in range(2, num+1):
        res.append(num % i)
    rs = list(set(res))
    rs.sort()
    if 0 in rs:
        rs.remove(0)
    return rs
def resolve2(num):
    res=[i for i in range(1,(num-3)//2+2)]
    return res
if __name__ == '__main__':
    # print(resolve2(2))
    flag=[False]*4
    print(flag)