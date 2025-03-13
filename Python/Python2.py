#carrying on from python1.py

#if you print a expression eg 3 > 5 it will return a boolean value
print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

a = 200
b = 30
if a > b: #if a is bigger than b it prints that it is with a if statement
    print("a is bigger than b")
else:
    print("b is bigger than a")

#you can use boolean to evaluate data
print(bool("Hello")) #both return true
print(bool(15)) 
#you can also do this with a variable

#most values are true except empty string and a value of 0 and any lists are true except empty ones

#all of these are true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#all of these are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass(): #class like a blueprint to assign values
  def __len__(self): #function that returns 0 or a false value
    return 0 #return is just giving the value back as a output not printed

myobj = myclass() #sets the variable to the class
print(bool(myobj)) #prints it as a boolean value

#function to print a boolean value
def myFunction() :
  return True

print(myFunction())

#you can print code or other things using the value outputted by a function/ the answer
def myfunction():
   return True #sets the value to true
if myfunction():
   print("It's true") #prints if the value is true
else:
   print("It's false") #prints if the value is false

#this says if its true or not if its the specified data type
a = 3
print(isinstance(a, int)) #if a is a integer prints true if not false
#isinstance checks if a variable is a specified data type

