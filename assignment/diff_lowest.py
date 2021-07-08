def low_diff(l):
    if not l:
        print("list empty")
        return 0
    else:
        l.sort()
        l=list(set(l))
        print(l[1]-l[0])
        return