#create a class
class MyClass:
    x = 5       
#create a object
p1 = MyClass() #instance of object MyClass
print(p1.x)
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
p2 = Person("leonidas",20)
print("Name: {}\nAge: {}".format(p2.name,p2.age))
