
def odd_num(l):
    if not l:
        print("list empty")
        return 0
    else:
        l.sort()
        print(l)
        if l[0]==l[1]:
            print(l[-1])
        
        else:
            print(l[0])
        return 1

        

"""l=[]
n=int(input("Enter no. elements"))
for i in range(n):
    l.append(int(input()))
odd_num(l)"""