# # in python
# if u do a = 3
# then a = 4

# a first points at 3 then points at 4 , like objects in java

# but in java if u do a = 3 then a = 4 , it just changes values

# because in java int is primitive not an object

# in python everything is an object


a = 2
a = 4

print(f"{id(2)}")
print(f"{id(4)}")


# 140736373803480
# 140736373803544

# u will get different ids because in memory , they are stored at different memory places

# so in python everything is an object , thus immutable
# like String arrays in java


mutable = set()
print(f"{id(mutable)}")
mutable.add(5)

print(f"{id(mutable)}")

# 1722544564800
# 1722544564800

# u will get the same , because set are mutable , that is they will be changed , they dont point to different location ,
# same location they are overriden


random = ("key 1" , "key 2" , "key 3")

(key1 , key2 , key3) = random

print(key1)
print(key2)
print(key3)


a , b = 2 , 3

print(a)
print(b)

# tuple are immutable

ans = "key 1" in random
# membership
print(ans) 


set1 = {'a' , 'a' , 'b' , 'e'}
set2 = {'c' , 'c' , 'd' , 'e'}

union = set1 | set2
intersection = set1 & set2
only_in_set1 = set1 - set2

print(union)
print(intersection)
print(only_in_set1)

# dict stores key value pairs

dict1  = {}
dict1["base"] = "cha1"

print(dict1)
print('base' in dict1)
print
del dict1['base']
print(dict1)

a = 5

b = 0 if a == 5 else 6
print(b)

list1 = ["a" , "b" , "c"]

for idx , item in enumerate(list1 , start=1):
    print(idx , item)

name = ['swaraj' , 'vinod' , 'mali']
bills = [7 , 21 , 13]


for item in zip(name , bills , list1):
    name , bill , random = (item)
    print(name , bill , random)
    print(item)


def demo_fn(*keys , **extras):
    print(keys)
    print(extras)


demo_fn(1 , 2 , num = 4 , num2 = 6)
# 1 and 2 will be keys and num and num2 will be extras
# ** means kwargs , keyword arguments , arguments which are sent with their keys like num and num2 here.


def chai(num1 , num2):
    print(num1)
    print(num2)

chai(num1 = 5 , num2= 6)

a = 5
b = 7

chai (num1= b , num2= a)



def random():
    return 100 , 20

A , B = random()

print(A , B)


print(A) if A == 100 else print(B)