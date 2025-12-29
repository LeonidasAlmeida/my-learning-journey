#local variables
def sum(x,y): #create a function
    sum = x + y # local variable
    return sum
print(sum(5,10))
del sum #delete a function sum
#global variables
x = 5
y = 10
def sum():
    sum = x + y
    return sum
print(sum())
