#Write a Program to generate 5 Random Numbers in the range 10 to 50
#Use Seed vale =6   
#Make a provision to change this seed value everytime you execute the program by associating with the time of execution 

import random

import time

random.seed(6)
random_number1 = random.randint(10, 50)
random_number2 = random.randint(10, 50)
random_number3 = random.randint(10, 50)
random_number4 = random.randint(10, 50)
random_number5 = random.randint(10, 50)

print("5 Random Numbers between 10 and 50:")
print(random_number1)
print(random_number2)
print(random_number3)
print(random_number4)
print(random_number5)


current_time=int(time.time())
print(current_time)

new_seed= 6 + current_time

random.seed(new_seed)

print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))

