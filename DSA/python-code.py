#these are fibonacci sequences adds the previous two numbers together to get the next number

prev2 = 0
prev1 = 1

#algorithm using a for loop 
print(prev2)
print(prev1)
for fibo in range(18):            #repeats for 18 times basically
    newFibo = prev1 + prev2       #adds the previous two numbers together
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo               #this and previous changes the previous numbers to the next numbers

#fibonacci using recursion
#recursion is calling itself inside itself
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2): #defines a function with the name fibonacci
    global count #defines it uses a global variable 
    if count <= 19: # if count is less or equal to 19
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2) #because it calls itself inside itself it will repeat uptil its told not to which is when the count is bigger than 19
    else:
        return

fibonacci(1,0)

#finding the n'th fibonnaci number using recursion
def F(n): #define function with name f
    if n <= 1: #if n is equal or less than 1 return n 
        return n
    else:
        return F(n - 1) + F(n - 2) #else return the function of n-1 plus n-2

print(F(19)) #print function 19 bascially the 20th number because in python the first number is 0 its called a 0 based index



#an algorithm can be used to find a specific value within the array for example the highest or lowest value


#arrays
#this is a list but can be used in the same way as a array in some aspects
myarray = [7, 12, 9, 2, 15]

print(myarray[1]) #prints the 2nd piece of data in the array because it uses a 0 based index which in this will output "12"


#making a algorithm to find the smallest number in a array
'''
Variable 'minVal' = array[0]
For each element in the array
    If current element < minVal
        minVal = current element
'''


#a algorithm based on the one above that finds the minimum value
minval = myarray[0] #sets the variable minval (minimum variable) to the arrays first value
for i in myarray: #i is a placeholder variable basically no value but says for each value in the array 'myarray'
    if i < minval: #for each value in the array if the value is smaller than minval
         minval = i #change minval to the smaller value
#so the end result is minval being the smallest value out of all the values in the array
print(minval)