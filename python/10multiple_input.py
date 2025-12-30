#muiltiple input 
args =["x","y","z"]
args[0],args[1] = input("Enter two values: ").split()
print("Number of boys:",args[0])
print("Number of girls:",args[1])
#taking three input at a time
args[0],args[1],args[2] = input("Enter three values: ").split()
print("Total number of estudens: ",args[0])
print("Number of boys is : ",args[1])
print("Number of girls is : ",args[2])
#taking two input at a time
a,b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a,b))
#taking multiple input at a time
x = list(map(int, input("Enter multiple values : ").split()))
print("List of students: ", x)
