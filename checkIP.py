import re
def checkIP():
    number = input('Enter what is displayed: ')
    #while True:
    ipv4 = re.search('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', number)
    ipv6 = re.search('(([a-f0-9:]+:+)+[a-f0-9]+)', number)
    if ipv4:
        print('4')
    elif ipv6:
        print('6')
    else:
        print('-1')
checkIP()

#This is a second function.
import ipaddress
def checkIP():
    number = input('Enter the number you have: ')
    try:
        iP = ipaddress.ip_address(number)
        if iP:
            print(iP.version)
    except:
        print('-1')
checkIP()
