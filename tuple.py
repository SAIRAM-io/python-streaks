# Empty tuple
my_tuple = tuple()
my_tuple = ()
print(my_tuple)

# Homogenous tuple
my_tuple = (1, 2, 3)
print(my_tuple)

# Heterogenous tuple
my_tuple = (1, "Hello", 3.6, [10, 20, True])
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# List to Tuple
my_list = [1,2,3,4]
my_tuple = tuple(my_list)
print(my_tuple)

# Tuple to List
my_tuple = (1,2,3,4)
my_list = list(my_tuple)
print(my_list)

# Tuple Packing
my_tuple = 10, "hello", False
print(my_tuple)

# Tuple unpacking
a, b, c = my_tuple
print(a)
print(b)
print(c)

# Indexing & Slicing
my_tuple = (1, 2, 3, [10, 20, 30], (15, 25, ('Hello', False), 35 ))
print(my_tuple[3])
print(my_tuple[4][2][1])
print(my_tuple[1:5])

# Modification --- We cant do modification
my_tuple = (1, 2, 3, 25, 'Hello', False, 35 )
print(my_tuple)
my_tuple[2] = 'New value'            # TypeError: 'tuple' object does not support item assignment
print(my_tuple)

# Concatenation & Repeat
tup1 = (1, 2, 3) 
tup2 = (4, 5, 6)
print(tup1 + tup2)

print(("Hello") * 3)        # HelloHelloHello
print(("Hello",) * 3)       # ('Hello', 'Hello', 'Hello')

# count()
my_tuple = (1, 2, 3, 2, 1, 4, 5,1,2, 3)
print(my_tuple.count(1))

# index()
my_tuple = (1, 2, 3, 2, 1, 4, 5,1,2, 3)
print(my_tuple.index(3))

# sorted()
my_tuple = (1, 2, 3, 2, 1, 4, 5,1,2, 3)
print(sorted(my_tuple))

# reverse
my_tuple = (1, 2, 3, 2, 1, 4, 5,1,2, 3)
print(my_tuple[::-1])