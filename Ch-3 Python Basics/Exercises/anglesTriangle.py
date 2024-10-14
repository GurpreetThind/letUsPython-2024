#Given three sides a b c of a triangle 
#Wite a program to obtain and print the vaues of three angles 
#round to the next integer


import math

a=4
b=3
c=5 

cos_C =((a**2)+(b**2)-(c**2))/(2*a*b)
cos_B =((a**2)+(c**2)-(b**2))/(2*a*c)
cos_A =((c**2)+(b**2)-(a**2))/(2*c*b)

angle_C=math.acos(cos_C)
angle_B=math.acos(cos_B)
angle_A=math.acos(cos_A)

degree_angle_c= math.degrees(angle_C)
degree_angle_b= math.degrees(angle_B)
degree_angle_a= math.degrees(angle_A)

angleA = math.ceil(degree_angle_a)
angleB = math.ceil(degree_angle_b)
angleC = math.ceil(degree_angle_c)

print(angleA)
print(angleB)
print(angleC)