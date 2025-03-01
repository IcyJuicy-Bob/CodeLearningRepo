#This is a comment

"""
this is a multi-line
comment python ignores
multi-line strings not
assigned a variable
so bascially a comment
"""

#no command for declaring a varible its made once you define a value
x = 4 #integer data type
print(x)
y = "test" #string data type
print(y)
#you can print strings without varibles
print("Hello World")
print(4)

#this is called casting
a = str(3) #stored as '3' (string)
b = int(3) #stored as 3 (integer)
c = float(3) #stored as 3.0 (floating-point or float)

#you can print the data type with the type function
print(type(c)) #will print float because the c variable is a float

#strings can be defines with either single or double quotes
z = "test"
z = 'test'

#varible names are case sensitive
a = "3"
A = "4"
#A wont overwrite a

#variables are case sensitive and can only incluse A-Z 0-9 and the underscore (_) they cant be any python keywords e.g. print

#multi word variables can be written in diffrent ways

#camel case - each word but the first word starts with a capital
myVariableName = 1
#pascal case - each word starts with capital
MyVariableName = 2
#snake case - each word is seperated by a underscore
my_variable_name = 3


#you can assign multiple variables in one line
x, y, z = 1, 2, 3
print(x, y, z)

#you can assign one value to multiple values
#you need to add a equals sign between each variable
a = b = c = 1
print(a, b, c)

#make a list use square brackets
fruits = ["apple", "banana", "pear"]
x, y, z = fruits #this sets each character to those in the list on the same postition
print(x) #print the variable to show the list values
print(y)
print(z)

#you can use the + operator to print multiple variables
x = "Hello " #there is a space at the end because the + jsut adds it to the end in words a space is needed to its not connected and looks weird
y = "world"
print(x + y)

#for numbers + works like in maths as a mathmatical operator
x = 3
y = 6
print(x + y, "this is the result of 3 + 6") #you can put text as well as variables in the print operator to print both a comma is needed to seperate them

#you can put both text and string in a print with a comma
print(x, z) #adding a comma instead of a + automatically leaves a space between the two items

#variables outside a function are global variables meaning they can be used in and out of variables
a = 3
def function1(): #defining a varible def says to define and function1 is my name of my function it needs the brackets and the colon to work
    print("value =", a) #then you say what you want the function to do in this it shows global varibles work in functions

function1() #calls a function and runs the function which i defined previously

