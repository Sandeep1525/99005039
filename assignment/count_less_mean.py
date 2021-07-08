
def mean_cnt(l):
    index=0
    if not l:
        print("Empty list")
        return 0
    else:
        mean=sum(l)//len(l)
        l.append(mean)
        l.sort()
        print(l)
        for i in range(len(l)):
            if mean==l[i]:
                index=i
        print(index-1)
        return 1

    