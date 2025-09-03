#1. Inheritance – "Reusing Code from a Parent Class"
#Inheritance allows a class (child) to inherit methods and properties from another class (parent).

class Animal:                           #Parent Class
    def speak(self):
        print("Animal Makes Voice")
    
class Bear(Animal):
    def roar(self):
        print("Bear Roars")

d = Bear()       #You create an object d of class Bear.
d.speak()        #You didn’t define speak() in the Bear class but but since Bear inherits from Animal, and Animal has a method speak(), it can still call it.
d.roar

# 1 Car drive
class Vechicle:
    def start(self):
        print("The Vechicle is started")

class Car(Vechicle):
    def drive(self):
        print("You can drive the car now")
    
car1 = Car()
car1.start()
car1.drive

#2 Area Calculator
class Area:
    def space(self):
        print("Calculating the area")

class Circle(Area):
    def area(self,radius):
        self.radius = radius
        a = 3.14 * radius * radius
        print(f"The area of Circle is {a}")

class Square(Area):
    def area(self,side):
        self.side = side
        a = side * side
        print(f"The Square is {a}")

c = Circle()   
s = Square()

c.area(4)         #giving value for the area  of c and c is assigned as Circle with radius
s.area(5)         #giving value for the area of c and c is assigned as Square with side


# 3 Constructor Inheritance

class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def show(self,grade):
        self.grade = grade
        print(f"The name is {self.name} and grade is {self.grade}")

student1 = Student("abc")   #only wrong in this else everything is right
student1.show(50)


#4 Animal Inheritance

class Animal:
    def __init__(speak):
        print("Animal Wth SOund")

class Cat(Animal):
    def cat(self):
        print("Cat Meows")
class Bear(Animal):
    def bear(self):
        print("Bear Roars")
class Sparro(Animal):
    def sparro(self):
        print("Sparrow speak")

cat1 = Cat()
cat1.cat()

bear1 = Bear()
bear1.bear()

sparro1 = Sparro()
sparro1.sparro()

#revision
#simple inheritance
 
class Animal:                          #parent node
    def speak(self):
        print("Animals Speaks")
class Bear(Animal):                    #here the Bear class is been inherited from the class animal so it has all the funcitons of the animal clas
    def bar(self):
        print("Bear Roars")

d = Bear()                             #creating the object for the class bear and the bear is been inherited from the animal hence it has all the functions of both classes
d.speak()
d.bar()


#Inheritance Using Person and Student Classes

class Person:
    def __init__(self,name):
        self.name = name

class Student(Person): 
    def __init__(self,name,grade,subject):      #it should be accroding to the sequence if name is first then we have to right name first
        super().__init__(name)          #calling the name from the person class 
        self.grade = grade 
        self.subject = subject
    def display(self):
        print(f"The Name Is {self.name} and Grades Is {self.grade},and the subject is {self.subject}")
    

name,grade,subject = input("Enter Your names grades and subjects ").split()
student1 = Student(name,int(grade),subject)
student1.display()    


#Polymorphism

'''Polymorphism means "many forms".
In programming, it allows the same method or function name to behave differently based on the object or class using it.'''

#1 using speak but differt forms 
class Animal:
    def speak(self):
        print("Animal Makes Sound")

class Cat(Animal):
    def speak(self):                   #Polymorphism 
        print("Cat Meows")
 
class Sparrow(Animal):                 #Polymorhpism
    def speak(self):
        print("Sparow sings")

animal1 = Cat()
animal2 = Sparrow()

animal1.speak()
animal2.speak()

#2 Polymorphism with Animals
class Animal:
    def speak(self):
        print("Animal Makes Sound")

class Cat(Animal):
    def speak(self):
        print("Cat Mewos")

class Bear(Animal):
    def speak(self):
        print("Bear Roars")

#Loop using polymorphism
for a in [Cat(),Bear(),Animal()]:
    a.speak()


#3 Polymorphism with Shapes

class Shape:
    def area(self):
        print("Calculating Area")

class Circle(Shape):
    def area(self):                       #ploymorphism
        print("Area of circke = πr²")

class Square(Shape):
    def area(self):                       #polymorphism
        print("Area of square = side * side")

for a in [Circle(),Square(),Shape()]:
    a.area()


#4 Polymorphism with Payment Systems

class Payments:
    def pay(self):
        print("Processing The Payment")

class Card(Payments):
    def pay(self):
        print("Paying with Credit card")

class Paypal(Payments):
    def pay(self):
        print("Paying With Paypal")

for transaction in [Card(),Paypal(),Payments()]:
    transaction.pay()


#5  Common Function Using Polymorphism

class Bird:
    def sound(self):
        print("Generic Bird Sounds")

class Parrot(Bird):
    def sound(self):
        print("Parrot says: Hello")

class Crow(Bird):
    def sound(self):
        print("Crow Says: Caw")

def make(bird):
    bird.sound()

make(Parrot())
make(Crow())


#Task 1 :  Animal Sounds
class Animal:
    def speak(self):
        print("Animals makes sound")

class Cat(Animal):
    def speak(self):                #Polymorphism
        print("Cat Meows")

class Cow(Animal):
    def speak(self):                #Polymorphism
        print("Cow Moos")

class Bear(Animal): 
    def speak(self):                #Polymorphism
        print("Bear Roars")

for animals in [Animal(),Cat(),Cow(),Bear()]:
    animals.speak()

#Task 2 : Media Player

class Media:
    def play(self):
        print("Playing the Default Music")

class Music(Media):
    def play(self):
        print("Playing the song")

class Video(Media):
    def play(self):
        print("Playing the video")
    

choice = input("Enter Your choice want to play ").lower()    #for the lowercase

if choice == "music":
    user = Music()
elif choice == "video":
    user = Video()
else:
    user = Media()

user.play()

#Task 3 : Payment Gateway

class Payment:
    def payment(self):
        print("Payment Gateway")

class Creditcard(Payment):
    def payment(self):
        print("Paid Via Credit Card")

class Upi(Payment):
    def payment(self):
        print("Paid Via Upi")

class Cash(Payment):
    def payment(self):
        print("Paid Via Cash")

for pay in [Payment(),Creditcard(),Upi(),Cash()]:
    pay.payment()


# Task 4 : Notifications

class Notifications:
    def send(self):
        print("Sending The Messages")

class Emailnotification(Notifications):
    def send(self):
        print("Email Sent")
    
class Smsnotificaion(Notifications):
    def send(self):
        print("Sms Sent")
class Pushnotification(Notifications):
    def send(self):
        print("Push Notification Sent")
    
msg = input("Enter Your Choice Email/Sms/Push").lower()

if msg == "email":
    msg = Emailnotification()

elif msg == "sms":
    msg = Smsnotificaion()

else:
    msg = Pushnotification()

msg.send()
    


# Task 4 : Shape Area

class Shape:
    def area(self):
        print("Area Calculator")
    
class Rectangle(Shape):
    def area(self,length,width):
        self.length = length
        self.width = width
        area = length*width
        print(f"The area of rectangle is{area}")

class Triangle(Shape):
    def area(self,base,height):
        self.base = base
        self.height = height
        area = 0.5 * base * height
        print(f"The area of Triangle is{area}")

choice = input("Enter Your Choice Rectangle/Triangle").lower()
if choice == "rectangle":
    length,width = map(int,input("Enter Your length and witdth using space").split())
    shape = Rectangle()
    shape.area(length,width)

else :
    base,height = map(int,input("Enter Base and Height").split())  #maps here changes each strings into an integer ex : [5,10]
    shape = Triangle()
    shape.area(base,height)