def freq(s):
    if s=="":
        print("empty string")
        return 0
    else:       
        d={}
        words=s.split()
        for i in words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        return 1

#freq("time is precious ") 