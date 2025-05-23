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
#\n just moves the text onto another line

#three types of number data types (integer, float, complex)
x = 1# integer - can be positive or negative of infinite length
y = 2.5 #float - positive or negative number containing one or more decimals
y2 = 8.7e4 #floats can also be scientific numbers containing e which is the same as a power of 10 for example 2e2 is 2 to the power of 10 squared so x100
z = 1j #complex - complex numbers are imaginary numbers using j as the imaginary part

#you can convert each data type into another by using the "type"() method

x = 1 #integer
a = float(x)
print(type(a))

import random #import the random module
print(random.randrange(1, 10)) #random.randrange tells it it uses the random module and its a rand(random) number in a range then you specify the range
#also this doesnt display the top numbers for some reason so 10 would be displayed ever its only 1-9

#if you specify a value using the constructor function but use the terminology to specify another itll follow the constructor function
a = int(3) #will be integer 3
b = int(3.8) #will be integer 3
c = int("3") #will be integer 3

x = float(1) #will be 1.0
y = float(2.8) #will be 2.8
z = float("3") #will be 3.0
w = float("4.2") #will be 4.2

x = str("s1") #will be 's1'
y = str(2) #will be '2'
z = str(3.0) #will be '3.0'

#using single or double quotes give the same result while defining strings
#you can use quotes inside quotes you just have to use the opisite type
print('text to show "quotes"')
#multiline quotes
print("""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""")
#the line breaks are still shown in the console
#like other languages strings are a array of bytes so use can call each character like a array
#python doesnt have a character data type its just a string with the length of 1
#square backets can be used to access elements of a string
a = "Hello World"
print(a[1]) #prints the character at postition 1 the first position is 0 so 1 is the second
#it will print 'e'
print() #line break

#you can also loop through strings
for variable in "banana": #for each character in banana
    print(variable) #print the character
#you can print the length of a string with the len(length) operator
print(len("Hello")) #prints the length of the string

#you can check if there is a phrase in the string
txt = "string to check phrase searches"
print("phrase" in txt) #there is the phrase 'phrase' in the string so it would output true

if "phrase" in txt: #you need colons on if statements btw
    print("there is the word 'phrase' in the variable") #prints the string if there is the word 'phrase' in the variable 'txt'

#you can do the same thing but if its not in the string by adding not before 'in'
txt = "string to check phrase searches"
print("random" not in txt) #there is not the phrase 'random' in the string so it would output true

if "random" not in txt:
    print("there is not the word 'random' in the variable") #prints the string if there is not the word 'random' in the variable 'txt'

#you can print only a certain range with the string
print("hello world"[2:5]) #will print 'llo' which is character 2-4 because in python is doesnt use the last number in a range
#same thing except it prints from the start instead of postition 2
print("hello world"[:5]) #will print 'hello' which is position 0 to 4
#same this except it prints from the end instead of position 5
print("hello world"[2:]) #will print 'llo world' which is position 2 to the end (12)

#you can do the same thing but from the end of the string using negative numbers
a = "Hello World"
print(a[-5:-2]) #-5 from the end is 'w' and -2 is 'l' but the last number isnt included so 'r' which would print W-r so 'Wor'

#string modifing

print(a.upper()) #you can modify sttrings using ."element"() in this case 'upper' this will display the string only in uppercase
print(a.lower()) #same thing goes for lower but it will print only in lowercase

b = " Hello World "
print(a.strip()) #you can use the strip element to remove any whitespaces before or after the string (spaces)

#you can replace letter in the strip using the replace element
print(a.replace("H", "J")) #replaces the specified letter with another letter specfied after characters are just length 1 strings so you have to specify them as a string

c = "Hello, World!"
print(c.split(",")) # splits the word into two "['Hello', ' World!']" at the specified point in this case ',' but it does replace that character with a comma so i would only do it on commands or it'll look a bit weird

#you dont have to do these with a variable for example
print("hello".upper()) #prints upercase without a variable
d = b.strip() #assigns a value but removing the outside whitespaces (spaces) first
print(d) #prints it

#string combining

a = "Hello"
b = "World"
c = a + b #combines them but doesnt leave room for a space
print(c)
c= a + " " + b #combines them but added a space in the middle dont forget the actual space inside the brackets btw
print(c)

#formatted strings

a = "age = "
#b = "a" + 46  this doesnt work to combine strings

age = 36
#f strings use curly brackets are used to hold placeholder variables inside the string
txt = f"age = {age}" #this is a f string it formats strings put a f before the string and it checks for curly brackets and uses that as a placeholder value
print(txt)

#a placeholder can contain variables, operations, functions, and modifiers to format the value
price = 59
txt = f"the price is {price:.2f}" #to define a modifyer use a colon : then a legal formatting type for this its .2f which is a fixed point number with length of 2 deicmals
print(txt)

print(f"math operations inside a placeholder (2 x 6) : {2*6}") #you can do math operations inside strings using formatting and output the value

#escape characters let you use symbols mainly quotes when you shouldnt be allowed
print("this is a \"quote\" in a string") #use the backslash as a escape character before teh character you want the string to ignore and print anyway
#there is also specific line commands you can use with the backslash
#\'	Single Quote	    outputs a single quote/apostrophe
#\\	Backslash	        shows a backslash like another other character
#\n	New Line	        rolls over to the next line
#\r	Carriage Return	    i think this is the same as a new line but the cursor is put at the begining of the new line so it just updates over the text on the new line
#\t	Tab	                inserts a tab around 4 spaces or something
#\b	Backspace	        same as a backslash on your keyboard deletes a space
#\f	Form Feed	        i dont really know what this does but it outputs like this          hello 
#                                                                                                  world
#\ooo	Octal value	    uses octal values to print characters "\110\145\154\154\157"
#\xhh	Hex value       uses hex values to print characters "\x48\x65\x6c\x6c\x6f"

#the next bunch of things i didnt write myself because there is a lot
#this is the stuff you use after a string for example a.upper()

#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning


#moved to python2.py because this is getting quite long