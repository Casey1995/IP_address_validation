import re
def checkIP():
    number = input('Enter your IP address: ')
    # Alternate IPv4 regex. ipv4 = re.search('(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', number)
    ipv4 = re.search('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', number)
    ipv6 = re.search('(([a-f0-9:]+:+)+[a-f0-9]+)', number)
    if ipv4:
        print('This is version 4')
    elif ipv6:
        print('This is version 6')
    else:
        print('Invalid IP')
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
