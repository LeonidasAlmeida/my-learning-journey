#packing and unpacking arguments in python
# * (fоr tuрlеѕ) аnd ** (fоr dictionaries).

#unpacking
def fun(a,b,c,d):
    print(a, b, c, d)
#drive code
my_list = [1,2,3,4]

fun(*my_list)

#packing
def mySum(*args):
    return sum(args)
print(mySum(1,2,3,4,5))
print(mySum(10,20))