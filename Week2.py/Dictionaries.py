#Dictionaries - A dictionary is a data structure in Python that stores data in key-value pairs.

dictionary = {'name':'Karan','age':21} #Here name is key and karan is value and age is key and 21 is value
print(dictionary) 

#Key Dictionaries Operations
#1 Accessing the value
print(dictionary['name'])

#also can be get as .get
print(dictionary.get('age'))

#2  Add / Update a key-value pair
dictionary['City'] = 'Mumbai'  #this will add new key value pair
print(dictionary)

dictionary['age'] = 22    #Here this will update the existing value
print(dictionary['age'])

#3 Delete a key
del dictionary['age'] #deleting the age from the dictionaries
print(dictionary)

#4 Iterate through a dictionary there are two types in it first for the key and second for value
for i in dictionary.keys():  #only iterate for the keys
    print(i)

# For values attribute
for j in dictionary.values():
    print(j)

# For key value pairs use items
for k,v  in dictionary.items(): #For Loop iterating for two values hence writtten as as kv
    print(k,":",v)   