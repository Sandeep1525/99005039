def mexican_wave(wave):
    word = ""
    if not type(wave)==str:
        print("Enter a string")
        return 0
    elif wave=="":
        print("entered an Empty string")    
    elif wave.islower():
        l=list(wave)
        for i in range(len(wave)):
            val = wave[i].upper()
            l[i] = val
            for i in l:
                word = word + i
            print(word)
            word = ""
            l = list(wave)
        return 1 

    else:
        print("enter lower case string")
        return 0

#n=input()
#mexican_wave(n)