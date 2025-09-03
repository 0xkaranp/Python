#String Methods

#1 strip()    :Removes leading and trailing spaces from a string.

text = "   Hello World    "
print(text)                   #When We do this the space is added 
print(text.strip())           #But using stript the space is removed

#2 split()    :Splits a string into a list of words using spaces (or any delimiter).

sentance = "Python is aws"
print(sentance.split())       #splitted the each words

#also can be done using this
data = "apple,water,fruit"
print(data.split(','))

#3 join()    :Joins elements of a list into a string using a separator.
words = ["python","is","aws"]
print(words)
print(''.join(words))      #double '' is for empty word if we put , then it will print , between them '' this is for no space

#4 find() :Finds the index of a substring. Returns -1 if not found.
message = "Hello Python"
print(message.find('Python'))  #returns the first index no of the word you enter and also counts spaces

#5 replace() : Replaces all occurrences of a word with another.'
syntax = "I love junk food"
print(syntax.replace("junk food","helthy food"))    

#6 upper() : Use to  convertt the string into lower case and lower() :Use for converting the stringg into upper case 
string = "hello"
print(string.upper())
string2 = "PYTHON"
print(string2.lower())
