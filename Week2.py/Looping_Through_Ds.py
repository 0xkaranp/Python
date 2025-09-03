#Basic For Loop
name = {"Juice","Fruits","Vegetables"}
for i in name:
    print(i)

#With index using enumerate() :When in a loop we want the value and index of the value at the same time we do use this method
name1 = {'Normal Cube','Mirror Cube','5 Layer Cube'}
for index,names in enumerate(name1):      #Here Two variables first because of first is for index and second for the its names
    print(index,names)                    #This will print the index and the names at same time 
    print(f"index{index}:{names}")   

#Task 1: Loop through a list and print each item with its index
names = {"asus","hp","lenovo"}
for index,name in enumerate(names):
    print(f"index at {index} : {name}")

#Task 2. Looping Through a Set  : Sets are unordered, so you can't access by index — just use a for loop:
set1 = {"red","green","blue"} 
for i in set1:
    print(i )

#Task 3  Looping through a Dictionary  :Dictonaries stores the value in key value pair
dictonary1 = {'name':'karan','age': 21}
for i in dictonary1.keys():       #This will print only keys 
    print(i)
for j in dictonary1.values():     #this will print only values hence use values() in last
    print(j)

for i,j in dictonary1.items():    #And to get both the values and keys we use items()
    print(i,j)

#Task 2: Loop through a dictionary and print keys and values
Grades = {
    'A' : 85,
    'B' : 90,
    'C' : 78
}
for i,j in Grades.items():
    print(f"The {i} score is : {j}")