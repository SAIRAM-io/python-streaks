# sets -- set() or {}
my_set = {1, 2, 3}
print(my_set)

# empty set
my_set = set()
print(my_set)

# we cannot use {} to create an empty set
my_set = {}
print(type(my_set))     # here an empty dictionary will be created

# sets cannot have duplicates
my_set = {1, 2, 3, 1, 2, 3}
print(my_set)           # {1, 2, 3}

# sets cannot have mutable objects
my_set = {1, 2, 3, [10, 20]}
print(my_set)           # Throw an error

# Set is an unordered collection, so it doesnot support indexing and slicing
my_set = {1, 2, 3}
print(my_set[0])        # TypeError: 'set' object does not support indexing

# adding single item
my_set = {1, 2, 3}
my_set.add('hello')
print(my_set)           # {1, 2, 'hello', 3}

# adding multiple items (items can be passed using lists, tuples or sets)
my_set = {1, 2, 3}
my_set.update([3, 4, 5, 6])    
my_set.update({3, 4, 5, 6})
my_set.update((3, 4, 5, 6))
print(my_set)           # {1, 2, 3, 4, 5, 6}

# discard() -- won't throw an error if element is not existing in set
# remove() -- will throw an error if element which we are trying to remove is not existing in set
my_set = {1, 2, 3, 4, 5}
my_set.discard(4)           # removes 4
my_set.discard(14)          # No error
print(my_set)

my_set = {1, 2, 3, 4, 5}
my_set.remove(4)            # removes 4
my_set.remove(14)           # Throws an error
print(my_set)

# Set Operations
# union operation -- a.union(b) or use | operator
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {10, 20, 3, 4, 50}
print(my_set_1 | my_set_2)
print(my_set_1.union(my_set_2))         # {1, 2, 3, 4, 5, 10, 50, 20}

# intersection operation -- a.intersection(b) or use & operator
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {10, 20, 3, 4, 50}
print(my_set_1 & my_set_2)
print(my_set_1.intersection(my_set_2))  # {3, 4}

# difference operation -- a.difference(b) or use - operator
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {10, 20, 3, 4, 50}
print(my_set_1 - my_set_2)
print(my_set_1.difference(my_set_2))  # {1, 2, 5}

# symmetric_difference operation -- a.symmetric_difference(b) or use ^ operator
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {10, 20, 3, 4, 50}
print(my_set_1 ^ my_set_2)
print(my_set_1.symmetric_difference(my_set_2))  # {1, 2, 5}
