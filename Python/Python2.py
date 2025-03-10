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