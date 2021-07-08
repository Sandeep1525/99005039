def max_by_deleting_digit(n):
    if len(str(n))==0:
        print("empty")
        return 0
    elif n>=0 and n<=9:
        print(n)
        return 3    
    elif type(n)!=int:
        print("Enter int")
        return 1    
    else:    
        l=[]
        while(n!=0):
            l.append(n%10)
            n=n//10
        l.reverse()
        l1=[]
        for i in range(len(l)):
            s = ""
            for j in range(len(l)):
                if i!=j:
                    s+=str(l[j])
            l1.append(int(s))
        print(max(l1))
        return 2


#max_by_deleting_digit(8976)