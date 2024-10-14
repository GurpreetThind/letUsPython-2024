#This code snippet teaches us how to import Module at basic level 

import math
import random

print(random.random())

print(math.floor(random.random()*1000000000000))
print(math.ceil(random.random()*1000000000000))
print(math.pi)
print(math.degrees(math.pi))
print(math.factorial(11))

###check builtin functions list 

import math

print(dir(__builtins__))

import random

print(dir(random))