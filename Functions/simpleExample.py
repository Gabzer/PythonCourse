#########Syntax#########
def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
        
by_three(3)
########################

#########Import#########
#one fonction
from math import sqrt

#Example
import math            # Importa o modulo math
everything = dir(math) # Converte tudo em uma lista de coisas de math
print everything       # Exibe tudo!
########################

###Built-in functions###
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

print type(2)           #<type 'int'>
print type(18.45)       #<type 'float'>
print type('coiso')     #<type 'str'>
########################