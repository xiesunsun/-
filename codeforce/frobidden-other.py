for _ in range(int(input())):
    s = list(input())
    t = input()
    if t == "abc":#如果是按照顺序且需要排列的话，那么一定是abc需要进行排列，我们讨厌循环要尽量避免循环操作
        # 所以直接的字符串替代会比在原串上改变高效的多
        s = ''.join(sorted(s))
        i_c = s.count("c")
        i_b = s.count("b")
        print(s.replace("a" + "b" * i_b + "c" * i_c, "a" + "c" * i_c + "b" * i_b))#这是一部精华的操作从第一个匹配的开始进行替换操作
    else:
        print("".join(sorted(s)))
