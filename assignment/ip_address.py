import ipaddress
def ip_int(num):
    if num=="":
        print("empty string")
        return 0
    else:    
        ip=ipaddress.ip_address(num)
        print(int(ip))
        return 1

#ip_int('121.120.255.1')