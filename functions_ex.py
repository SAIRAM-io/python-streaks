# Function is a group of logically related statements that performs a specific task.
# We define functions using 'def'

def greet():    # function defination
    """
    This function greets to the user
    """
    print("Hello, User")

greet()         # function call

# Parameters -- values that function catch at function defination
# Arguments -- Real values that we pass to function at function call
def greet(name):
    print('Hello, {}!!'.format(name))

greet('Harsh')

# Types of Arguments:
# 1) Positional arguments 
def greet(name, message):
    print('Hello {}, {}'.format(name, message))

greet('Harsh', 'Good Morning!!')

# 2) Keyword arguments 
def greet(name, message):
    print('Hello {}, {}'.format(name, message))

greet(message='Good Morning!!', name='Harsh')

# 3) Default arguments
def greet(name, message='Good Morning!!'):
    print('Hello {}, {}'.format(name, message))

greet('Harsh')
greet('Harsh', 'Good Evening!!')

# 4) Arbitrary arguments
def greet(*names):
    for name in names:
        print('Hello, {}'.format(name))
    
greet('Harsh', 'Priya', 'Chaitan', 'Amit')

def greet(message, *names):
    for name in names:
        print('Hello {}, {}'.format(name, message))
    
greet('Good morning!!', 'Harsh', 'Priya', 'Chaitan', 'Amit')

def set_user(**details):
    for det in details.items():
        print(det[0], '==>', det[1])
    
set_user(name= 'Harsh', age= 21, courses= ['Physics', 'Chemistry'])

# Local variables & Global variables
num = 10
def some():
    global num
    num += 100
    print(num)
some()
print(num)

# Recursive Function -- Function calling itself
def sample(num):
    print(num)
    if num < 10:
        sample(num+1)           # function calling itself
sample(5)

# example
def factorial(num):
    if num==1 or num==0:
        return 1
    return num*factorial(num-1)
print(factorial(5))

# example
def my_func(colors):
    if len(colors) == 1:
        print("Color :", colors[0])

    else:
        mid = len(colors) // 2
        left = colors[:mid]
        right = colors[mid:]

        my_func(left)
        my_func(right)

colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow', 'Purple', 'Indigo', 'Orange', 'Violet']
my_func(colors)

# Lambda functions -- an anonymous function that is defined without a name.
# lambda variables : return statement
plus100 = lambda num : num + 100
print(plus100(5))

# lambda with map()
nums = [1,2,3,4,5,6,7,8,9]
res = list(map(lambda num: num ** 2 , nums))
print(res)

# lambda with filter()
nums = [1,2,3,4,5,6,7,8,9]
res = list(filter(lambda num: num%2==0 , nums))
print(res)