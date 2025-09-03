#Week 2 Data structures in python
list = [1,2,3,4,5,'apple']
print(list)

#Opertations in list
#1 Index
print(list[0])  #indexing the first element is been printed

#2 slicing 
print(list[0:3]) #This will print only the elements at index pos 0 to 3

#3 Appeand
list.append("juice")  #this will add juice in the end of the list in this we can also put the elements in a specific locatio by this syntac inser(indexat,element_name)
print(list)    

#4 Remove
list.remove(1)   #This Will remove 1 from the list and to print updated array we have to print it 
print(list)

#Pop in remove
list.pop() # This will remove the last item from the list
print(list) #remove the juice from the list

#Delete in Remove 
del list[0]
print(list) #This will delete the elements by the index

#5 Sorting
num = [4,6,7,1,3,9,10]
num.sort()               #This will be sort the numbers in ascending order
print(num) 

num.reverse()  #This will be giving us output in desecending order
print(num)

