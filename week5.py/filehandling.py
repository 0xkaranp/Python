#File Handling And Error Control
#File Handling 
#Reading and writing text files(Basic)
# Writing to a file (will create if not exists)
file = open("example.txt","w")  #Here we have created an file because it is not existed before with "w" means with write mode
file.write("Hello,File World")
file.close()                    #This will mandatory for the after writing into the file

#Reading from the file
file = open("example.txt","r")   #here we have open an existing file with variable r which indicates read
content = file.read()            #store the read contents of the file to the variable content
print(content)                   #printed the content
file.close                       #closing the file after the all 

#1 write
with open("example.txt","w") as file:
    file.write("This will be overwritten over the exist")     #this just creates a file and adds the new content and clears all the previous content
    file.close

#2 Appeand
with open("example.txt","a") as file:           #appeand for the the adding the new examples to text
    file.write("\nHello this is adding an new items to the previus file")
    file.close

#3 Read
with open("example.txt","r") as file:       #here it will cause the error if file not exist
    content = file.read()              
    print(content)

#4 Create Mode(Will cause error if already exist)
try:
    with open("example.txt","x") as file:             #If us just creates the new file it will create the a new file but it is already exist then it will give an error using that except block
        file.write("New file is created using 'x' mode")
except FileExistsError:
    print("File already Exist")


# writing list in mulitple lines
list = ["first\n","second\n","third"]

with open("multilines.txt","w") as file:
    file.writelines(list)                 #writelines() method is used to write a list of strings to a file.

#Reading the file

with open("multilines.txt","r") as file:
    for a in list:
        print(a.strip())

# Task 1 : Create and Write to a File

with open("notes.txt","w")as file:              #when we use with open it will automatically close the file no need to close the file
    file.write("Python Is Powerful\nFile handling is easy \nPractice make Perfect")
    
with open("notes.txt","r")as file:
    content = file.read()
    print(content)

list = ["Python is Powerfull\n"
        "File handling is easy\n"
        "Practice Makes Perfect"]

with open("listfile.txt","w")as file:
    file.writelines(list)                   #here writelines is predefined librarry
# Task 2 : Read from the file and show output
with open("listfiles.txt","r") as file:
    for a in list:
        print(a.strip())
    
# Task 3 :  Append More Notes

with open("new.txt","w")as file:
    file.write("Hello this is new file")
   
with open("new.txt","a")as file:
    newline = input("Enter New Lines You want to add ")
    file.write("\n" + newline)    

with open("new.txt","r")as file:
    new = file.read()
    print(new)

# Task 4 : Count Total Lines in File
with open("new.txt","r") as file:
    lines = file.readlines()
    print("Total lines is",len(lines))

# Task 5 :  Custom File Creator

createfile = input("Enter your file name that You want to create with extension.txt ")

try:
    with open(createfile,"x") as file:
        file.write("New File Here")
except FileExistsError:
    print("File Already Exist")

with open(createfile,"r")as file:
    new=file.read()
    print(new)