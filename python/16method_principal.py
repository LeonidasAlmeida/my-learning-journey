class Person:
    games = 50
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"name : {self.name} age : {self.age} game: {self.games}"

p1 = Person("John",36)
print(p1.games)