#dictionay data type
#creting empty dictionary
Dic = {}
print(Dic)
#creating dictionary with integer keys
Dic ={
    1:'michael',
    2:"For",
    3:"michael"
}
print(Dic)
print(*Dic) #when the keys is integer we must use just * and when is diferent(string) we must use ** for unpacking
#
Dict = dict([(1, 'michael'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)
#
dic =dict([("name", 'michael'), ("number", 'For')])
print(dic.get("name"))
print(dic["number"])