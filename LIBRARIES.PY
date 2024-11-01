
from math import *
print(sin(radians(90)))

# 
import datetime as x
print(x.datetime.now())


from random import randint
print(randint(1,100))

try:
    import non_existing_Module
except ImportError:
    print("Module not found")

import os
(os.mkdir("new_dictionary"))
print(os.listdir())
(os.rmdir("new_dictionary"))
print(os.listdir())

import sys
print("Current Python version is: ",sys.version)
print("Command line arguments are:",sys.argv[0])

import math
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
ans=math.gcd(a, b)
print(f"The gcd of {a} and {b} is:",ans)
print(f"The factorial of {ans} is:",math.factorial(ans))

import random
list=[]
for i in range(5):
    num=random.randint(1, 50)
    list.append(num)
print("The list is: ",list)

import datetime
date=datetime.date.today()
print("Current date is: ",date)
earlier_date = date - datetime.timedelta(days=100)
print("Date before 100days is:",earlier_date)
print(f"The day on the {earlier_date} is:",date.weekday())
print("Monday=0 to Sunday=6")


from mypackage import *
print(module1(1,2))
print(module2(2,4))