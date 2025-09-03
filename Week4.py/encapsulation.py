#Encalpuslation
'''Encapsulation means bundling data and methods that operate on that data into a single unit (a class) and restricting direct access to some of the class's components.'''
#Examples :
#1 . Public Members - accessible for everyone
'''self.name = "karan"'''

#2 . Protected Members – prefix with _, suggest it’s for internal use
'''self._salary = 50000'''

#3 . Private Members – prefix with __, restrict access
'''Self.__bankbalance = 100000'''

#Example 1 : Without encapuslations

'''class Person:
    def __init__(self,name,age):
        self.name = name                 #public
        self.age = age                   #public

person1 = Person("karan",20)

print(person1.name)   #ok 
print(person1.age)    #ok

person1.age = -10     #here the the age cannot be negative but it is modified and age is negative 

print(person1.age)
'''
#To solve this problem Encapsulation comes 
class Person:
    def __init__(self,name,age):
        self.name = name
        self._age = age  #private use

    def getage(self):           #Getter : To access a private variables value
        return self._age
    
    def setage(self,age):       #setter : To update __age safely means here less than 0 age is not allowed And setter here will have diffrent name the getter
        if age>0:
            self._age = age
        else:
            print("Invalid Age")

p = Person("karan",21)
print(p.getage())

p.setage(20)
print(p.setage)

#Tasks
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age            #private

    def getage(self):
        return self.__age
    
    def setage(self,age):
        if age > 0:
            self.__age = age

        else:
            print("Invalid age")
    
person1 = Person("karan",21)

print(person1.getage())        #safe access

person1.setage(-5)             #Here it will give error as invalid age and will print the old age as same
print(person1.getage())


# Task 1 :  Student Marks Validator

class Student:
    def __init__(self,marks):
        self.__marks = marks

    def getmarks(self):
        return self.__marks
    
    def setmarks(self,marks):
        if  marks >= 0 and marks<=100:
            self.__marks = marks
        else:
            print("Invalid Marks")

student1 = Student(30)

print(student1.getmarks())

student1.setmarks(110)
print(student1.getmarks())


#Task 2 : Bank Account with Balance Check

class Bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance 

    def getbalance(self):
        return self.__balance
    
    def setdeposit(self,balance):
        if balance >= 0:
            self.__balance = self.__balance + balance
        else:
            print("same amount")
        
    def setwithdraw(self,balance):
        if balance > self.__balance:
            print("Insuffiecient Balance")
        else:
            self.__balance = self.__balance - balance

person1 = Bankaccount("karan",5000) 
print(person1.getbalance())

person1.setdeposit(2000)
print(person1.getbalance())

person1.setwithdraw(2000)
print(person1.getbalance())


# Task 3 : Salary Setter with Minimum Check

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def getsalary(self):
        return self.__salary
    
    def setsalary(self,salary):
        if salary >= 8000:
            self.__salary = salary
        else:
            print("Salary is To low")

emp1 = Employee("abc",9000)
print(emp1.getsalary())
emp1.setsalary(10000)
print(emp1.getsalary())    
emp1.setsalary(5000)
print(emp1.getsalary())    


# Task 3 : Product Price Update

class Product:
    def __init__(self,name,price):
        self.name = name
        self.__price = price
    
    def getprice(self):
        return self.__price
    
    def setprice(self,newprice):
        if newprice > 0:
            self.__price = self.__price + newprice
        else:
            print("Same price update")

pro = Product("abc",2000)
print(pro.getprice())
pro.setprice(0)
print(pro.getprice())

# Task 5 : Email Validation
class Employee:
    def __init__(self,name,email):
        self.name = name
        self.__email = email

    def getemail(self):
        return self.__email
    
    def setemail(self,check):
        if "@" in check and "." in check:
            print("Email is validated it contains @ and .")
        else:
            print("Email is Not validated")

email1 = Employee("abc","abc@gmail.com")
print(email1.getemail())
email1.setemail("abc@gmail.com")
print(email1.getemail())
