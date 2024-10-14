#this snippet shows how a same obj can be reference by different variable 

a=30
b=30

print(id(a))
print(id(b))


print(a is b)
"""
Both a and b are refering to same object 30 of class int 

140706009529688
140706009529688
True
"""