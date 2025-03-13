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
print(0)
print(1)
count = 2
#comment on this i havent don eit yet im more intrested iin pokemon
def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(1,0)
