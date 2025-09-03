#Tupples In Python,tupples are same as list but they are immutable means it cannnot be changed or modified after been created

tuples=(2,3,4,)  #The syntax diffrence between and tuple and a list is it is round braces
print(tuples)

#tuples.append("apple")
#print(tuples)           #This will not add the items in the end because it is tuple the cannot be changed

print(tuples[1])
print(tuples[0])
print(tuples[2]) #Will print the the elements of the tuples

for items in tuples:
    print(items)

#Conversion of Tupples to list and vice versa

newlist = list(tuples)    #This list keyword converts the tuples into the list
print(newlist)

newlist.append(5)   #Now we can easily modify the string
print(newlist)