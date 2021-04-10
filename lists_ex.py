# empty list
my_list = []
my_list = list()

# Homogenous list
my_list = [1, 2, 3]

# Heterogenous list
my_list = [10, 3.36, "Hello", True]

# Duplicate values list
my_list = [10, 3.36, 10, "Hello", True, True, "World", 3.36]

# Nested list
my_list = ["Happy", [10, 3.36], [True, False], "Birthday"]

# List indexing and Slicing
colors = ['red', 'blue', 'green', 'white', 'black']
print(colors[1])
print(colors[1:4])
print(colors[:4])
print(colors[1:])

# Negative indexing
print(colors[-1])
print(colors[-3:-1])

# Get no. of elements - len()
print(len(colors))
colors[5] = 'something'               # throws an error
print(colors)

# Insertion of elements
colors = ['red', 'blue', 'green']
colors.append('yellow')
colors.append('white', 'black')         # throws an error
colors.append(['white', 'black'])
print(colors)

# Concatenation of lists - (+ operation)
# Concatenated  and stored in another list
colors1 = ['red', 'blue', 'green']
colors2 = ['white', 'black']
colors = colors1 + colors2
print(colors)

# Concatenation of lists - extend()
# Concatenated and stored in 1st list
colors1 = ['red', 'blue', 'green']
colors2 = ['white', 'black']
colors1.extend(colors2)
print(colors1)


# Modification
colors = ['red', 'blue', 'green', 'white', 'black']
print(colors)
colors[2] = 'yellow'
print(colors)

# Lists & loops
colors = ['red', 'blue', 'green', 'white', 'black']
for color in colors:
    print("Color", color, sep=' => ')
    
for ind in range(len(colors)):
    print("Color {} => {}".format(ind, colors[ind]))

ind = 0
while True:
    if ind == len(colors):
        break
    print("Color {} => {}".format(ind, colors[ind]))
    ind += 1

# Lists - membership operators
colors = ['red', 'blue', 'green', 'white', 'black']
print('red' in colors)
print('yellow' not in colors)

# Insert(index, value)
my_list = [10,15,45,89,63,54,25,20,77,78]
print(my_list)
my_list.insert(5,'hello')
print(my_list)

# pop(index)
my_list = [10,15,45,89,63,54,25,20,77,78]
val = my_list.pop()         # Removes last element
print(val, my_list)
val = my_list.pop(1)        # Removes 1st index element
print(val, my_list)
val = my_list.pop(-1)       # Removes last index element
print(val, my_list)

# remove(element)
my_list = [10,15,45,89,63,54,25,20,77,78]
print(my_list)
my_list.remove(15)
print(my_list)

# clear() -- makes list empty
my_list = [10,15,45,89,63,54,25,20,77,78]
print(my_list)
my_list.clear()
print(my_list)

# index(element, start, end)
my_list = [10,15,45,89,63,54,25,20,77,78]
ind = my_list.index(15)
print(ind)
ind = my_list.index(63, 3, 8)
print(ind)

# count()
my_list = [10,15,45,10,89,63,45,54,63,25,10,20,25,77,78]
cnt = my_list.count(10)
print(cnt)

# sorted(list_name) & list_name.sort()
my_list = [10,15,45,10,89,63,45,54,63,25,10,20,25,77,78]
my_list.sort()
print('Ascending order:',my_list)
my_list.sort(reverse=True)
print('Descending order:',my_list)

# Reversing a list - reverse & list_n[::-1]
my_list = [10,15,45,10,89,63,45,54,63,25,10,20,25,77,78]
print(my_list[::-1])
my_list.reverse()
print(my_list)

# string to list
a = "hello"
print(list(a))

# list to string
a = [11,22,33]
b = '--'.join(a)
print(a)

# taking multiple values as input in one line
abc = list(map(int, input().split()))
print(abc)

# == vs is
num1 = [1,2,3]
num2 = [1,2,3]
print(num1 == num2)
print(num1 is num2)

num1 = [1,2,3]
num2 = num1
print(num1 == num2)
print(num1 is num2)

# copy()
num1 = [1,2,3]
num2 = num1
num1.append(4)
print(num1)					# [1, 2, 3, 4]
print(num2)					# [1, 2, 3, 4]

num1 = [1,2,3]
num2 = num1.copy()          # num2 = num1[:]
num1.append(4)
print(num1)					# [1, 2, 3, 4]
print(num2)					# [1, 2, 3]

# List comprehension
even_nums = [i for i in range(20) if i%2 == 0]
print(even_nums)

even_or_odd = ['even' if i%2 == 0 else 'odd' for i in range(20)]
print(even_or_odd)

res = []
[res.append(i) for i in range(20)]
print(res)

even, odd = [], []
[even.append(i) if i%2 == 0 else odd.append(i) for i in range(20)]
print(even)
print(odd)