def iso(name):
    if name=="":
        print("Empty string")
        return 0
    elif type(name)==int:
        print("enter a string")
        return 0    
    else:    
        l = list(set(name))
        cnt = 0
        for i in l:
            if i.isalpha():
                cnt += 1
        if cnt == len(name):
            print("is isogram")
        else:
            print("not isogram")
        return 1

#iso("abcd")