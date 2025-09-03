'''Day One Of Python Programming'''
'''
a = "karan"
age = 21
height = 168

print(a,age,height)

string = "10"
b = int(string)+5
print(b)
'''
'''Take 2 numbers as input and print:'''
'''
A = input("Enter A Number")
B = input("Enter another Number")
A = int(A)
B = int(B)
C = A + B
D = A - B
E = A * B
print("The additon is: ",C)
print("The subtraction is",D)
print("The mul is:",E)
'''
'''Operators and user Input'''
'''
a = input("Enter A Number")
b = input("Enter Another Number")
a = int(a)
b = int(b)
print("The additon is:",a+b)
print("The subraction is: ",a-b)
print("THe mul is",a*b)
print("The div is",a/b)
print("The remainder is: ",a%b)
print("The floor division operator is",a//b)
print("The power is",a**b)'''

''' Task 2: Comparison Operators Quiz'''
'''
a = input("Enter A Number")
b = input("Enter another number")

a = int(a)
b= int(b)

if(a==b):
    print("it is equal")
elif(a!=b):
    print("It is not equal")
elif(a>b):
    print("A is greater than B")
else:
    print("B is greater")


'''
'''Task 3: Logical Operators Test'''
'''
a = input("Enter a number")
b = input("Enter another number")

a = int(a)
b = int(b)

if(a > 0 and b > 0):
    print("It is positive number")
else:
    print("It is not positive number")
if(a > 0 or b > 0):
    print("Any of the number is positve")
else:
    print("Both is negative number")
'''
'''Can Vote Or Not'''
'''age = input("Enter The age ")
age=int(age)
natio = input("Enter Your Nationalitly ")
natio = str(natio)
if age >= 18 and natio == "ind":
    print("You Can Vote")
else:
    print("You Can Not Vote)'''

'''Day 4 Strings and String functions'''
'''name = input("Enter Your Name")
print(f"hello,{name}!") 
just name will not works
print(name.upper())
print(name.lower())
print("Reversed text",name[::-1])
Here [::-1 is start:stop:direction and here start not define start from end and stop at begining
'''
'''Replace Vowels with *'''
'''
text = input("Enter Your Text")
vowels = "aeiou"
for ch in vowels:
    text=text.replace(ch,"*")
print("After replacing the vowels",text)
'''
'''
Slicing 
text = input("Enter Your Text")
print("The slice string is",text[:3])
print("Last 2 letters are",text[-2:])
print("Every Second letter is ",text[::2])
'''
'''
text = input("Enter Your name: ")
word = input("Enter the word you want to find: ")

new = text.find(word)

# Print the result
print(f"'{word}' found at position {new}" if new != -1 else "Word not found")

replace = input("Enter the number You want replace")
print("The replace word is",text.replace(word,replace))
'''

'''
'''
''' Challenge Task: Word Censor Tool'''
string = input("Enter Your String ")
banned_words = "boring,powerfull"
words = banned_words.split(",")
for ch in words:
    string=string.replace(ch,"***")
print("After replacing the vowels",string)


