from functools import reduce

my_list = [1,2,3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
print(reduce(accumulator, my_list, 10))


# lambda expressions: functions that you use only once

# square
my_list = [5,6,7]
sq_list = map(lambda x: x**2, my_list)
print(list(sq_list))

# List sorting based on second item in the tuple
a = [(0,2), (4,3), (10,-1), (9,9)]
a.sort
print(a) # this has sorted the list based on first item in the tuple
a.sort(key=lambda x: x[1])
print(a)


#############################################################################

my_list = []
for char in 'hello':
    my_list.append(char)
print(my_list)

###################

my_list = [char for char in 'hello']
print(my_list)

my_list = [num**2 for num in range(0,10)]
print(my_list)

#printing all even numbers
my_list = [num for num in range(0,10) if num%2 == 0]
print(my_list)

my_list = {num for num in range(0,10)}
print(my_list)


#####################

simple_dict = {
    'a' : 2,
    'b' : 3
}
my_dict = {key:value**3 for key,value in simple_dict.items()}
print(my_dict)
########################

simple_dict = {
    'a' : 2,
    'b' : 3
}
my_dict = {key:value**3 for key,value in simple_dict.items() if value%2 == 0}
print(my_dict)

##########################