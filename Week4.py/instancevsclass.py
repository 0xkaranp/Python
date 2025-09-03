#Instance vs Class Variables
# Instance variable : all the concept we've learn in the classes and objects is instance variable / A instance variable is variable which is only been used for that specific object
#Class Variable: A class variable is shared across all instances of a class. While a class can have multiple instances (objects), there is only one copy of the class variable, and it is shared by all those instances.

#1 instance variable example

class Car:
    def __init__(self,brand,model):
        self.brand = brand         #instance variable
        self.model = model         #instance variable
    def disp(self):
        print(f"Brand : {self.brand} and model : {self.model}")

brand,model = input("Enter Your brand and model").split()
car1 = Car(brand,model)

car1.disp()

#2 Class Variables

class Mobiles:
    camera = 50                #Class Varible

    def __init__(self,brand):
        self.brand = brand     #Instance Variable
    
    def disp(self):
        print(f"The Brand is {self.brand} ")

mobile1 = Mobiles("Motorola")

mobile1.disp()
print(f"and it has camera of {mobile1.camera}mp")     #Printing the class variable and we can also print it in the def disp
Mobiles.camera = 10
print(f"and it has camera of {mobile1.camera}mp")


#3 Track the Number of Objects Created

class Student:
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count = Student.count+1
        print(f"The total count is {Student.count}")

    
student1 = Student("A")       #if we dont create and class for printing it is also fine we can also do like this
student2 = Student("B")

#4 Inventory

class product:
    discount = 10

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def apply_discount(self):
        a = self.price/10
        cost = self.price - a
        print(f"The discounted price after discount is{cost}")

pro = product("Mouse",250)

pro.apply_discount()


#5 Employee Salary Tracker

class Employee:
    companyname = "Techcorp"
    def __init__(self,name,salary,bonus):
        self.name = name
        self.salary =salary
        self.bonus = bonus
    
    def emp(self):
        a = self.salary+self.bonus
        print(f"The name is {self.name} and salary is {self.salary} and bonus is {self.bonus} and salary after bonus is {a} from {Employee.companyname}")

name,salary,bonus = input("Enter Your Name Salary and Bonus ").split()
emp1 = Employee(name,int(salary),int(bonus))

emp1.emp()

#6 Library Book Tracker

class Book:
    libraryname = "Central Library"

    def __init__(self,title,author):
        self.title = title
        self.author = author
    def out(self):
        print(f"The Title is {self.title} its author is {self.author} and library name is {Book.libraryname}")

title,author = input("Enter Book Title and Author").split()
custo1=Book(str(title),str(author))

custo1.out()
        

#7 Student Grade Book

class Student:
    school = "ABC High School"

    def __init__(self,name,math,science):
        self.name = name
        self.math = math
        self.science = science
    
    def summary(self):
        avg = (self.math + self.science) / 2
        print(f"The School is {Student.school} and name of student is {self.name} and average marks is {avg}")
        
name,math,science = input("Enter Your Name Math and Science marks ").split()

student1 = Student(name,int(math),int(science))

student1.summary()

#8  Modify Class Variable from Object

class Animal:
    species = "Canine"
    
    def __init__(self,name):
        self.name = name
    def disp(self):
        print(f"The {self.name} belongs to {self.species}")
    
animal1 = Animal("Bear")
animal1.species = "Wolf"
animal1.disp() 
