import re

def checkIP():
    number = input('Enter what is displayed: ')
    while True:
        ipv4 = re.search('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', number)
        ipv6 = re.search('(([a-f0-9:]+:+)+[a-f0-9]+)', number)
        if ipv4:
            print('4')
            break
        if ipv6:
            print('6')
            break
        else:
            print('-1')
            break
checkIP()
