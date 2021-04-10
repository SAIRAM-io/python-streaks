'''
	An exception is an event, which occurs during the execution of a program 
	that disrupts the normal flow of the program's instructions.
	if these exceptions are not handled, programn will crash.
	We use try-except block for handling such exceptiopns
'''
# Basic example
a, b = 20, 0
try:
    print(a/b)
except:
    print("Something went wrong!!")


# To know which exception is raised, we use err.__class__
nums = [1,2,3,4]
try:
    print(nums[100])        # IndexError
    print(2/0)              # ZeroDivisionError
except Exception as err:
    print("Something went wrong!!")
    print(err.__class__)


# Some commonly occuring exceptions
'''
	ImportError	-- Raised when the imported module is not found.
	IndexError -- Raised when the index of a sequence is out of range.
	KeyError -- Raised when a key is not found in a dictionary.
	NameError -- Raised when a variable is not found in local or global scope.
	TypeError -- Raised when a function or operation is applied to an object of incorrect type.
	ValueError -- Raised when a function gets an argument of correct type but improper value.
	ZeroDivisionError -- Raised when the second operand of division or modulo operation is zero.
'''

# To catch specific exceptions
import math
nums = [1,2,3,4]
try:
    print(nums[100])
    print(2/0)
    a = b
    a = math.sqrt(-10)
except IndexError as err:
    print("Check your Index Range again!!")
except ZeroDivisionError as err:
    print("You cannot divide a number with zero!!")
except NameError as err:
    print("You have not initialized some variables. Please check!!")
except Exception as err:
    print(err.__class__)
    print("Something went wrong!!")

# When we want to execute some code when there is no errors in try block, we use "else"
a,b = 120, 10
try:
    print(a / b)
except Exception as err:
    print(err)
else:
    print('Try block is executed successfully')
print('Outside try-except')

# We have finally block which will be executed even error occured or not
# we use finally block to release external resources like database connections.
a,b = 120, 0
try:
    print(a / b)
except Exception as err:
    print(err)
finally:
    print('The finally block')
print('Outside try-except')

# Raise your own exceptions - raise()
try:
    age = -20
    if age <= 0:
        raise ValueError("Age cannot be negative!\nPlease try again")
except ValueError as err:
    print(err)

# User-defined exceptions - Example 1
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

num = 250
try:
    if num < 100:
        raise ValueTooSmallError
    elif num > 500:
        raise ValueTooLargeError
except ValueTooSmallError:
    print("The value is too small, try again!")
except ValueTooLargeError:
    print("The value is too large, try again!")
else:
    print("Congratulations! You guessed it correctly.")


# User-defined exceptions - Example 2 
class ValueTooSmallError(Exception):
    message = ''
    def __init__(self, num):
        self.message = '{} is smaller than 100'.format(num)

class ValueTooLargeError(Exception):
    message = ''
    def __init__(self, num):
        self.message = '{} is greater than 500'.format(num)

num = 50
try:
    if num < 100:
        raise ValueTooSmallError(num)
    elif num > 500:
        raise ValueTooLargeError(num)
except ValueTooSmallError as err:
    print(err.message)
except ValueTooLargeError as err:
    print(err.message)
else:
    print("Congratulations! You guessed it correctly.")


# User-defined exceptions - Example 3
class WrongValueError(Exception):
    message = ''
    def __init__(self, num, flag):
        if flag == 0:
            self.message = '{} is smaller than 100'.format(num)
        else:
            self.message = '{} is greater than 500'.format(num)
num = 1250
try:
    if num < 100:
        raise WrongValueError(num, 0)
    elif num > 500:
        raise WrongValueError(num, 1)
except WrongValueError as err:
    print(err.message)
else:
    print("Congratulations! You guessed it correctly.")

