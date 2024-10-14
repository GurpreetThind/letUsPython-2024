#Write a program that makes use of trignometric functions available in math module

import math 
print(dir(math))

angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print(math.sin(angle_radians))
print(math.cos(angle_radians))

angle_degrees = 90
angle_radians = math.radians(angle_degrees)
print(math.sin(angle_radians))
print(math.cos(angle_radians))

print(math.cosh(angle_radians))