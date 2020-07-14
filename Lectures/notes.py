# ​names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]

# s_names = [name.capitalize() for name in names if name[0].lower =='s']
# ​print(s_names)

names = ["Sarah", "same", "Frank", "bob", "Shawn", "sandy"]
# print(names)
s_names = [name.capitalize() for name in names if name[0].lower == 's']
# print(s_names) ## empty []

#calendar 
import sys
import calendar
from datetime import datetime

print(sys.argv)

l = len(sys.argv)

if l == 1:
    month = datetime.now().month
    year = datetime.now().year
if l == 2:
    month = int(sys.argv[1])
    year = datetime.now().year
if l == 3:
    month = int(sys.argv[1])
    year = int(sys.argv[2])
else:
    print('Error wrong characters entered.')

cal = calendar.TextCalendar()
cal.prmonth(year, month)
#####

'''
understand plan execute reflect
'''
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
''' 
build python classes store and category and complete with:
__init__() __str__() __repr__()

class car 
    methods(verbs): refuel() getFuel setSpeed() getSpeed() drive()  
    attributes(nouns): fuel maxspeed engine 
'''
