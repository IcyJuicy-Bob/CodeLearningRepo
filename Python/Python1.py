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

#variables outside a function are global variables meaning they can be used in and out of functions
a = 3
def function1(): #defining a varible def says to define and function1 is my name of my function it needs the brackets and the colon to work
    print("value =", a) #then you say what you want the function to do in this it shows global varibles work in functions

function1() #calls a function and runs the function which i defined previously

#if you assign a variable a value inside a function it will be local only changing inside the function not affecting the variable outside the function
def myfunc(): #defining a function
    a = 4 #setting the value of the variable
    print("value =", a) #printing the variable

myfunc() #calling the function

#if you use the global keyword inside a function the variable value wont be local like default it will be global
b = 2 #assign first global value

def myfunction2():
    global b #use the global keyword to say to assign the variable value as a global value
    b = 3 #assigned the value
    print(b)

myfunction2() #call the function


print("")
#extended range of data types
a = "hello world" #string data type for words
print(a)
print(type(a)) #prints the data type

b = 2 #integer data type for numbers 
print(b)
print(type(b)) #prints the data type

c = 2.5 #float data type for number with a decimal
print(c)
print(type(c)) #prints the data type

d = 1j #complex data type for complex numbers and imaginary numbers j replaces a i in python for imaginery numbers for some reason
print(d)
print(type(d)) #prints the data type

e = ["one", "two", "three"] #list data type makes lists to display or contain multiple values in a variable can be used to store integers strings and others
print(e)
print(type(e)) #prints the data type

f = ("one", "two", "three") #tuple data type stores multiple values it is ordered and unchangable
print(f)
print(type(f)) #prints the data type

g = range(6) #range data type these are to display a range of values of a data type
print(g)
print(type(g)) #prints the data type

h = {"name" : "mark", "age" : 36} #dict/dictionary data type used for mapping purpose has a key and a value for each eg age : 36
print(h)
print(type(h)) #prints the data type

i = {"apple", "banana", "pear"} #set data type stores unordered unique elements nulls arent allowed
print(i)
print(type(i)) #prints the data type

j = frozenset({"apple", "banana", "pear"}) #same as the set data type except they cant be changes after creation
print(j)
print(type(j)) #prints the data type

k = True #bool/boolean data type either a True or False value capitals are needed to define these
print(k)
print(type(k)) #prints the data type

l = b"hello" #bytes data type converts the string into binary data i think atleast couldnt find a good explanation
print(l)
print(type(l)) #prints the data type

m = bytearray(5) #byte array data type is a array of bytes used to store binary data
print(m)
print(type(m)) #prints the data type

n = memoryview(bytes(5)) #memory view data type is a way to view the contents of bytes and byte arrays is a changeable/modifiable sequence
print(n)
print(type(n)) #prints the data type

o = None #none data type represents the absence of a value
print(o)
print(type(o)) #prints the data type


#in this print command it tells you how to specify each data type
print("\n to specify a data type you use a constructor function \n for example str would be the function here (str'hello world') \n here are all the types of constructor functions same order as the types listed above \n str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray")

