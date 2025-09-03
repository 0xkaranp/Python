#Functions and Modules
# 1. Defining Functions & Return Values : A function is a block of reusable code that runs when you call it.
def greet():          #Here We defined a function
    return "Hello!"   #this will return Hello 
print(greet())          #and this will print the funcition

# 2.Parameters, Default & Keyword Arguments
#parameters
a = int(input("Enter number"))
b = int(input("Enter number"))
def addition(a,b):               #Here We firstly defined the parameters with input
    return a+b                   #Perform addition to it
print(addition(a,b))             #and then again called the funcition to print the output

#Default Keyword
#A default argument is a value that a function parameter takes if no value is passed during the function call.

name = input("Enter Your Name")
def greet1(name="User"):
    return f"Hello {name}"
print(greet1(name))

def greet2(name="User"):
    return f"Hello {name}"
print(greet2())                     #Here by default user is printed because of no paramters where given
print(greet2("karan"))              #Print hello karan because of input is given in greet

# Keyword Arguments
   #When you call a function, you can pass arguments in two ways:
   #Positional arguments based on order
   #Keyword arguments based on parameter names

def student(name,age):
    print(name,age)       #according to to parameters

student(age = 21,name="karan") #Here order dont matter you can either pass name first or age 

#3 Scope: Local vs Global

a = 10  #Global Scope

def word():
    a = 5      #here the a is been written under the function hence it is local scope
    return a
print(word())
print(a)

y = 100
def function1():
    y = 50
    return f"This is local scope {y}"
print(function1())
print(f"This is global scope {y}")

# 4 *args and **kwargs
# What is *args?
# *args allows a function to accept any number of positional arguments (arguments without keywords).
# The arguments are received as a tuple.

def add(*nums):
    return sum(nums)           #Here we cannot user int input because it do not have anything to store like this 1,2,3
print(add(1,2,3))  


#What is **kwargs in Python?
#**kwargs stands for "keyword arguments"
#It allows your function to accept any number of keyword arguments
#The function receives them as a dictionary

def name(**data):             #** for the args
    for key,value in data.items():
        print(key,":",value)
name(name="karan",age=21)

#question 2
def student(**details):
    print("Student details")
    for key,value in details.items:
        print(f"{key.title()}:{value}")
student(name="A",grade="A",Marks=85)

#when to use function paremeters : when we have give an external command then we use paremeters
# Task 1 : Maximum Numbers
a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))
def max_number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
print(f"The biggest number is {max_number(a,b,c)}")

#2 Even or Odd
a = int(input("Enter Number "))
def even(a):
    if a%2==0:
        return "It is even Number "
    else:
        return "It is an odd number"
print(even(a))

#3 Calculator with *args

def multilpy(*nums):
    if not nums:
        return 0
    
    result = 1
    for n in nums:
        result *= n
    return result
print(multilpy(1,2,3))

#4 Student Info with **kwargs
''''''
def student_info(**data):
    for key,value in data.items():
        print(f"{key} : {value}")
student_info(key="karan",value = 21)
''''''
import math
#5 Bmi Calculator

height = int(input("Enter Your height"))
weight = int(input("Enter Your weight"))

def bmi(height,weight):

    return round(weight/(height ** 2),2)   #Predefined function from the puthon round and last 2 is not in the formula it is for round upto 2 decimals

print(f"the Bmi is{bmi(height,weight)}")

#6 Return vs Print
def square(n):       #for logic use return not print and if want to display something then use print
    return n*n
print(square(3))


