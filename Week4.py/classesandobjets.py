#Class = Blueprint (like a plan of a house)
#Object = Actual thing created from the class (like the house built from that blueprint)

#1 Person Class
class person:
    def __init__(self,name,age):   #this is constructor to intialize the objects
        self.name = name
        self.age = age
    
    def greet(self):               #method(Behavior)  
        print(f"Hello this is {self.name} and my age is {self.age}")

#create a object now
person1 = person("karan",21)
person2 = person("darshan",26)

person1.greet()
person2.greet()



#2 Animal Class with Species and Sound Behavior
class Animal:
    def __init__(self,species,legs):
        self.species = species
        self.legs = legs
    
    def sound(self):
        print(f"The {self.species} makes sound and it has {self.legs} legs")

species,legs = input("Enter species name and legs").split()      #using inputs
animal1 = Animal(species,int(legs))

species,legs = input("Enter species name and legs").split()      #using inputs
animal2 = Animal(species,int(legs))

animal1.sound()
animal2.sound()

# Taks

#1 Car classes
class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def show_details(self):   #Methods(What will show)
        print(f"Brand : {self.brand} Model : {self.model} Year : {self.year}")

car1 = Car("Toyota" , "Fortune" , 2021)  # Normal Without input

car1.show_details()

brand,model,year = input("Enter the brand , model and Year").split()
car2 = Car(brand , model ,int(year))
car2.show_details()

#2 Student Class
#check_pass() → if marks ≥ 40: print "Pass", else "Fail"

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def check_pass(self): 
        if self.marks >= 40:                            #the marks is assign to self.marks hence we to write self.marks
            print("Congratulations You Are Passed")
        else:
            print("You are failed")

name,marks = input("Enter Your Name and Marks").split()
student1 = Student(name,int(marks))

student1.check_pass()

#3 Book class

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def summary(self):
        print(f"{self.title} by {self.author} and it is {self.pages} long")

title,author,pages = input("Enter Title,author and pages").split()
book1 = Book(title,author,int(pages))

book1.summary()

#4 Bank Account
 
class Bank:
    def __init__(self,accountname,balance):
        self.accountname = accountname
        self.balance = balance

    def deposits(self,amount):
        self.balance = self.balance+amount
        print(f"The balance after deposits is {self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient balance,your balance is {self.balance} cannot withdraw {amount}")
        else:
            self.balance = self.balance-amount
            print(f"The balance after withdraw is {self.balance}")
    
    def show_balance(self):
       print(f"The balance is {self.balance}")
    
accountname,balance = input("Enter Your Accountname and balane").split()
account1 = Bank(accountname,int(balance))


account1.show_balance()
account1.withdraw(500)
account1.deposits(3000)
account1.show_balance()


#5 Employee Salary Calculator

class Employee:
    def __init__(self,name,base_salary,bonus,balance=0):
        self.name = name
        self.base_salary = base_salary
        self.bonus = bonus
        self.balance = balance
    def total_salary(self):
        self.balance = self.base_salary + self.bonus
        print(f"The total salary is {self.balance}")

account1 = Employee("karan",10000,5000)

account1.total_salary()