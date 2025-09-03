#Basic Error Handling with try-except

'''Python gives an error (called an exception) when something goes wrong during
execution — like dividing by zero, or accessing a missing dictionary key.'''

# Syntax :
'''try:
    # risky code here
except:
    # what to do if error occurs'''

#Example 1:
try:
    num = 0
    result = num/0   #So this will cause zerodivisionerror in python so avoid this error we will user try except
except ZeroDivisionError:
    print("You Cannot Divide It By Zero")

#Task 1 :  Handle KeyError in dictionary
key1 = {'name':'karan','age':21}

try:
    print(key1['Grade'])    #So here we dont have created any key name grade this will cause the keyerror in python
except KeyError:
    print("Key Not Found")
    
#Task 2 : Handle invalid input using try-except
try:
    age = int(input("Enter A Number "))
    print(f"Your age is {age}")
except ValueError:
    print("Please Enter An Integer")

#Try Catch And finally
try:
    print("Trying")              #this will be printed because of the its not causing any error
    num1 = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by Zero") #After receving the error printed this
finally:
    print("this will always run") #this will be printed