def date(d):
    m30=[4,6,9,11]
    m31=[1,3,5,7,8,10,12]

    if d=="":
        print("Empty string")
        return 0
    elif type(d)!=str:
        print("Enter a string")
        return 1 
    else:
        dd,mm,yyyy=d.split("/")
        dd=int(dd)
        yyyy=int(yyyy)
        mm=int(mm)
        if mm>12:
            while mm>12:
                yyyy+=1
                mm=mm-12        
        if mm in m30:
            while dd>30:
                dd=dd-30
                mm=mm+1
            while mm>12:
                yyyy+=1
                mm=mm-12
            print(str(dd)+"/"+str(mm)+"/"+str(yyyy))    
            return 5
        elif mm in m31:
            while dd>31:
                dd=dd-31
                mm=mm+1
            while mm>12:
                yyyy+=1
                mm=mm-12
            print(str(dd)+"/"+str(mm)+"/"+str(yyyy))    
            return 5
        else:
            while dd>28:
                dd=dd-28
                mm=mm+1
            while mm>12:
                yyyy+=1
                mm=mm-12
            print(str(dd)+"/"+str(mm)+"/"+str(yyyy))    
            return 5


#date("36/24/2019")   