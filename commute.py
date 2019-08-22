"""
commute.py

calculate time spent on commuting to work for a year

"""

import sys


i=input("How long do you spend long commuting to work? (one way, in mintues) ")
m=int(i)

i=input ("How many days a week do you work? ")
d=int(i)

i=input("How many PTOs do you have? ")
p=int(i)


i=input("How many holidays do you have? ")
h=int(i)

c=m*(d*52-h-p)*2
hour= c//60
minute=c%60

print(f'You spend {hour} hours and {minute} minute(s) on commuting to work in a year! ')


sys.exit(0)
