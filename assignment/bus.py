def people_bus(o,d):
    if not o and not d:
        return 0
    elif not o:
        return 1
    else:
        print(sum(o)-sum(d))
        return 2

#n=int(input("Enter no of stations"))
"""o=[]
d=[]
for i in range(n):
    o.append(int(input("Enter no. of people onboarding at each station")))
for i in range(n):
    d.append(int(input("Enter no. of people departing at each station")))"""

#people_bus(o, d)