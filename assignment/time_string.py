def time_format(time):
    hrs,mins,secs= time.split(':')
    hrs=int(hrs)
    mins=int(mins)
    secs=int(secs)
    while secs>60:
        secs=secs-60
        mins=mins+1
    while mins>60:
        mins=mins-60
        hrs=hrs+1
    while hrs>23:
        if hrs==24:
            hrs=0
        else:
            hrs=hrs-23
    print(str(hrs)+":"+str(mins)+":"+str(secs))        
    return 1 

#time_format("23:73:95")