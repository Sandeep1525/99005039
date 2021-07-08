def mean_close(l):
    index=0
    if not l:
        print("Empty list")
        return 0
    else:
        mean=sum(l)//len(l)
        l.append(mean)
        l.sort()
        for i in range(len(l)):
            if mean==l[i]:
                index=i
        print(l[index+1],l[index-1])
        return 1

"""l=[]
n=int(input("Enter no. elements to add"))
for i in range(n):
    l.append(int(input()))
mean_close(l)"""                
