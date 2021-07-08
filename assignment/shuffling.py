def shuffle(num):
    if len(str(num))<=0:
        print("Empty number")
        return 0
    elif num<0:
        print("Enter a +ve number")
        return 2

    elif num<=9:
        print(num)
        return 1    

    else:
        l=[]
        while num!=0:
            l.append(num%10)
            num=num//10
        s=""
        l.sort(reverse=True)
        for i in l:
            s=s+str(i)
        print(s)
        return 3


#shuffle(911536)     