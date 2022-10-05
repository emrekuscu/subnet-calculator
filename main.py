from logging import root


ip = input("whats your ip?")
iparray = ip.split(".")
subnet_mask = input("whats your subnet mask?")
subnet_maskarray = subnet_mask.split(".")
cidr = input("Whats your CIDR?")
usablehost = 2**((32) - int(cidr)) - 2
print("Usable Host Range:" + str(usablehost))


print("Your Network Adress",end=":")
print(str(int(subnet_maskarray[0]) & int(iparray[0])),end = ".")
print(str(int(subnet_maskarray[1]) & int(iparray[1])),end = ".")
print(str(int(subnet_maskarray[2]) & int(iparray[2])),end = ".")
print(str(int(subnet_maskarray[3]) & int(iparray[3])))
 
 #usable host ip range





if int(iparray[0]) < 127 :
    print("Your Class: A")
elif int(iparray[0]) > 128 and int(iparray[0]) < 191 :  
    print("Your Class: B")
else:
    print("Your Class: C")


    #min max ipleri hesaplıcaz babag