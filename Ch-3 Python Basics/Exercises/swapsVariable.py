#Write a program that swaps the value of variables a and b 
#You are not allowed to use a third variable 
#You are not allowed to perform arithmetic operations 

a=10 
b=5 
print('a:',a)
print('b:',b)

print(id(a))
print(id(b))

a,b=b,a
print(id(a))
print(id(b))

print('a:',a)
print('b:',b)