# text = "helloworld"
# print(text.upper())

# text = "HELLOWORLD"
# print(text.lower())

# text = "hello world"
# print(text.strip())

# text = "hello world"
# print(text.replace("world", "there"))

# text = "hello world"
# print(text.split(" "))

#formate string

# Name= "ritik"
# age = 20
# print(f"my name is {Name} and my age is {age}")

# x = 5
# x+=3
# print(x)

# x = 10
# x-=2
# print(x)

# x = 10
# x*=2
# print(x)

#comparion operators

# x=5
# y=10
# print(x==y)
# print(x!=y)
# print(x>y)  
# print(x<y)
# print(x>=y) 
# print(x<)


#student["age"]=21
#student["city"]= "delhi"
#print(student)

#if else

# age = 21
# if age >= 21:
#     print("you are adult")       
# else:
#     print("you are not adult")

# age = 16

# if age>18:
#     print("you are adult")

#     elif age==18:
#         print("you are teen")

#         else:
#             print("you are not adult")


# x=15

# if x>10:
#     print("x is greater than 10")

#     if x>20:
#         print("x is greateryhan 20")
    
#     else:
#         print("x is not greater than 20")

# x = 8

# if x/2:
#     print("x is even number")

# else:
#     print("x is not even number")


# x=9

# if x%2:
#     print("x is odd number")

# else:
#     print("x is not odd number")


# # word= "python"

# # for x in word:
# #     print(x)


# # for i in range(1,10,4):
# #     print(i)


# # for i in range(1,4):
# #     for j in range(1,3):
# #         print(f"i{i},j={j}")


# # for i in range(1,6):
# #     if i ==4:
# #         break
# #     print(i)

# # for i in range(1,20):
# #     print(i)


# # for i in range(1,30):
# #     if i%2 == 0:
# #         print(i)

# # list1 = ["yello","blue","black"]

# # print(list1)


# #python functions


# # }!"def greet(name):
# #     print(f"hello, {name)

# # greet("alice")
# # greet("bob")


# # def add(a,b):
# #  return a - b

# # result = add(5,3)
# # print(result)

# def add(a,b):
#  return a * b

# result = add(5,3)
# print(result)


# def greet(name ="student"):
#    print(f"hello, {name}!")

#    greet()
#    greet("ritik")


# x = 10


# def myfunc():
#     y=5
#     print("inside",x,y)
# myfunc()
# print("outside",x)


# def greet():
#     print("hello")

# greet()


# #OOPS IN PYTHON
# class car:
#    def __init__(self,brand,color):
#      self.brand= brand
#      self.color = color

#    def drive(self):
#         print(f"{self.brand} is driving")

# #object

# car1 = car("bmw","black")
# car2 = car("defender","white")


# car1.drive()
# car2.drive()


#python array


# import array

# number= array.array('i',[1,2,3,4,5])
# print(number)


# from numpy import random

# x=random.randint(100)
# print(x)


# x=random.rand()
# print(x)

# import numpy

# from numpy import random
# x=random.choice([1,2,3,4,5])
# print(x)


# x=random.randint(100,size=(5))
# print(x)


# x=random.randint(100,size=(3,5))
# print(x)

 #python pandas

import pandas as pd

data = [10,20,30,40]
s=pd.Series(data)

print(s)
