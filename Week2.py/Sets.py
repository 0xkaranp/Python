# Sets (they are be written in the curly braces)
#1 Unordered : Meaning: The items in a set do not maintain the order in which you added them.

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Might print: {1, 2, 3, 4, 5}

my_set = {6, 1, 2, 3 ,4, 5}   #order wise it should be print 6 first but it printed the order according to ascending order
print(my_set)

#2 Unindexed
set1 = {1,2,3,4,5,6,7} 
# print(set1[0])    #This will cause the error becuase set is not indexilically order

for i in set1:
    print(i)     #This will print the list

#3 Unique
set2 = {1,1,2,2,3,3,4,4,5}
print(set2)                  #This will remove the repeted duplicate numbers only have the unique values

#Operation in Sets

# Add Elements
set3 = {'apple',2,5}
set3.add("onion")       #This will add an element in the last
print(set3)

# Remove Elements
set3.remove("onion")
print(set3)

# Set operations like union,intersection,diffrence
set4 = {1,2,3}
set5 = {3,4,5}

print(set4.union(set5))
print(set4.intersection(set5))    
print(set4.difference(set5))   