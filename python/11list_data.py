#list  data type
## append()add ond e end of list
## insert(index,value) add in expecific place
## extend(list) add a several values in a list
#empty list
List = []
print(List)
del List
#list with value
List = ['michealmick']
print("\nList with the use of String")
print(List)
#creating a List with
#the use multiple values
List =["micheal","mick"]
print("\nList containing multiple values: ")
print(List[0])
print(List[1])
#creating a multi-dimensional List
#(By nesting a list inside a list)
List = [['micheal'],['Geeks']]
print("\nMulti - Dimensional List")
print(List)
#adding element of list
List =[1,2,3]
print(List)
print(len(List))
List2 = [4,5]   
x =6
List.append(x)
print(List)
for i in List2:
    List.insert(len(List)-1,i)
print(List)
List.extend(List2)
print(List)
List.remove(4)
print(List)
List.pop()
print(List)
List.pop(1)
print(List)
