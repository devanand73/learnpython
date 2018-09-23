
import bs4
# 'generic import' of math module
import math
print math.sqrt(25)
######################
# import a function
from math import sqrt
print sqrt(25)    # no longer have to reference the module
#######################
# import multiple functions at once
from math import cos, floor
##############################
# import all functions in a module (generally discouraged)
from csv import *
#########################
# define an alias
import datetime as dt
#########################
# show all functions in math module
print(dir(math))
print(dir(bs4))

