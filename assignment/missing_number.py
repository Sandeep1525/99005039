def missing(ol,ml):
    if not ol:
        print("original list empty")
        return 0
    elif not ml:
        print("modified list empty")
        return 1
    else:
        for i in ol:
            if i not in ml:
                print(i)
        return 2

"""ol=[]
ml=[]
n=int(input("Enter no. elements"))
for i in range(n):
    ol.append(int(input()))
for i in range(n):
    ml.append(int(input()))
    
missing(ol, ml)"""