# list comprehension
# FOR COMPREHENSIONS , start reading from first for loop

colors = ['red' , 'blue' , 'green' , 'yellow']


filtered = [color for color in colors if len(color) == 3]

print(filtered)

# [result -> for -> if ]
# [expression for item in iterable if condition]
#start reading from "for"


# set comprehension


colors = ['red' , 'blue' , 'green' , 'yellow' , 'red']

color_set = {color for color in colors}

print(color_set)
# unique colors only

random_set = {
    "key1" : [2 ,4 ,5 , 33],
    "key2" : [24 ,48 ,53 , 233],
    "key3" : [26 ,42 ,534 , 433],
}

val_set = {val for values in random_set.values() for val in values if val > 100}

# for values in random_set.values() is the list 
# values is [2 , 4 , 5 , 33] and so on , its a list
# for val in values , val here is 2 , then 4 then 5...
# if is the condition on val
# u can do this even in list comprehension.
print(val_set)

# dict comprehension

products = {
    "bat" : 100,
    "ball" : 50,
    "gloves" : 80
}

result = {product:price for product , price in products.items()}

# [key:value for iteam in iterable if condition]
# its not necessary that after for , if will come , u can add for then for then if also.
print(result)

# generator

sales = [3,5,2,2,5,67,22,4,7,68,42,21]

random = [sale for sale in sales if sale >10]

print(random)
# this will make a list in the memory instantly

# but if we use generator which is
random = (sale for sale in sales if sale > 10)

print(random)
# gives a generator object which passes/stores values in memory one by one thus mostly used for memory optimizations
# Generators in Python are a clean way to create iterators without storing all values in memory at once. They’re especially useful for large datasets or streams of data.
# random is now an iterable
for rand in random:
    print(rand)

# will get an error because generator comprehensions can only be used once.
# as we already used it above for rand in random , if we do next(random) , we will get an error
print(next(random))

print(next(random))

print(next(random))

print(next(random))

