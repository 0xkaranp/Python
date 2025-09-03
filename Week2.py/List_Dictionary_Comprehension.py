# What is Comprehension : It’s a shortcut for creating lists or dictionaries from existing sequences (like range() or other lists) using a clean one-liner syntax.


#List comprehension
#Syntax is : [expression for item in iterable]

squares = [x*x for x in range(1,6)]  #so here we first calculate the its square and then write the for loop with itss range
print(squares)                       #This is known as code comprehension


# It is similar to this code
'''square = []
for i in range(1,6):
    square.append(i*i)  
print(square)'''

#Tasks on this : Create a list of squares from 1 to 10
square =[j*j for j in range(1,11)]
print(square)


# Dictonaries comprehension

#syntax : {key_expression: value_expression for item in iterable}
cubes = {k:k**k for k in range(1,6)}   #there sequence may vary because of the dictiories do not stroe data in linear order
print(cubes)                            #In this we have creted an key value pair not just value pair

# Tasks on this : Create a dictionary mapping numbers to their cubes
cube = {d : d ** d for d in range(1,11)}
print(cube)