# Exception Handling
'''
#1 Try and Except
try:
    x = int(input("Enter A number"))
    a = 10 / x
    print(f"The division is {a}")
except ZeroDivisionError:
    print("Can't Divide By Zero")
except ValueError:
    print("Enter A Valid Value")

#2 Try Except and finally

try:
    num = int(input("Enter A Number "))
    res = 10 / num
    print(f"Result is {res}")
except ZeroDivisionError:
    print("You Cant't Divide It By Zero")
except ValueError:
    print("Enter an number") 
finally:                     
    print("Program finished")


# Task 1 : Simple Division Calculator

try:
    a = int(input("Enter A Number"))
    b = int(input("Enter A Number"))
    c = a/b
    print(f"The division is {c}")
except ZeroDivisionError:
    print("Cannot Divide By Zero")
except ValueError:
    print("Enter Correct Number")
finally:
    print("Program Finished")


# Task 2 : File Reader with Error Handling

try:
    new = input("Enter Your File Name ")
    with open(new,"r") as file:
        new1 = file.read
        print(new1)
except FileNotFoundError:
    print("File Not Found")
finally:
    print("Program Finished")

# Task 3 :  Custom Exception with raise

try:
    age = int(input("Enter Your Age"))
    if age < 0:
        raise ValueError("Age Cannot Be Negative")
    else:
        print(f"Your age is {age}") 
except ValueError as e:                  #Here this for storing the value error which is been raise by cutom error
    print("error",e)
finally:
    print("Program Finished")

# Task 4 : New custom Error
class UnderAge(Exception):     #For Custom Error It is Mandatory to make class like this
    pass

try:
    age = int(input("Enter Your Age"))
    if age < 18:
        raise UnderAge("You are not 18")       #Custom Error
    else:
        print("You are above 18")

except UnderAge as e:                          #Custom Error
    print(f"Error! {e}")

finally:
    print("Program Finished")


# Task 5 : Marks Error 
class MarksError(Exception):
    pass

try:
    marks = int(input("Enter Your Marks "))
    if marks < 0 or marks > 100:
        raise MarksError("Enter A Valid Marks ")
    else:
        print(f"Your Marks is {marks}")

except MarksError as e:
    print(f"Error! {e}")

finally:
    print("Program Finished")

# Task 6 : Login System

class LoginError(Exception):
    pass

try:
    username = input("Enter Your Username ")
    password = int(input("Enter Your Password "))

    correct_username = "admin"
    correct_password = 1234

    if username != correct_username or password != correct_password:
        raise LoginError("Your Login Id Or Password Is Not Correct")
    else:
        print(f"Your Username is {username}")
        print(f"Your Password is {password}")

except LoginError as e:
    print(f"Error! {e}")

finally:
    print("End of login attempt")



# Task 7 : Calculator with Menu

class Calculator(Exception):
    pass

try: 
    a = int(input("Enter a number"))
    a != ValueError 
    b = int(input("Enter a number "))
    b != ValueError
    choice = input("Enter Your Choice")

    if choice == "addition":
        c = a+b
        print(f"The additon is {c}")
    elif choice == "subtraction":
        c = a-b
        print(f"The subtration is{a-b}")
    elif choice == "multiplication":
        c = a*b
        print(f"The multiplication is {a*b}")
    else:
        c = a/b
        print(f"The division is {c}")
finally:
    print("program end'''

# login error

class Loginerror(Exception):
    pass

try:
    username = input("Enter Your Username ")
    password = int(input("Enter Your Password "))

    correctusername = "admin"
    correctpassword = 1234

    if username != correctusername or password != correctpassword:
        raise Loginerror("You have enter wrong username or password")
    else:
        print(f"The username is {username}")
        print(f"The password is {password}") 

except Loginerror as e:
    print(f"error {e}")

finally:
    print("Program Fineshed")
