# To get the binary code of any values: bin(10)

''' OPERATORS '''
# Arithmetic Operators
# +, -, *, /, %, // - floor/integer division, ** - Exponentiation
a, b = 5, 2
print("a + b = {}".format(a + b))
print("a - b = {}".format(a - b))
print("a * b = {}".format(a * b))
print("a / b = {}".format(a / b))
print("a % b = {}".format(a % b))
print("a // b = {}".format(a // b))
print("a ** b = {}".format(a ** b))

# Comparison operators
# >, >=, <, <=, ==, !=
a, b = 20, 15
print("a < b : {}".format(a < b))
print("a > b : {}".format(a > b))
print("a <= b : {}".format(a <= b))
print("a >= b : {}".format(a >= b))
print("a < b : {}".format(a == b))
print("a > b : {}".format(a != b))

# Logical operators
# and, or, not
a, b = True, False
print("a and b : {}".format(a and b))
print("a and b : {}".format(a or b))
print("Negation of a : {}".format(not a))
print("Negation of b : {}".format(not b))

# Bitwise operators
# &, |, ~, ^, >>, <<
a, b = 2, 4
print("a & b : {}".format(a & b))
print("a | b : {}".format(a | b))
print("~a : {}".format(~a))
print("a ^ b : {}".format(a ^ b))
print("a >> 2 : {}".format(a >> 2))
print("a << 2 : {}".format(a << 2))

# Assignment operators
# +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=
num = 10
num += 5	# num = num + 5
print(num)


# Identity operators
# is , is not
a, b = 10, 20
print("a is b : {}".format(a is b))
print("a is not b : {}".format(a is not b))

# Membership operators
# in, not in
city = "hyderabad"
print("y in hyderabad : {}".format('y' in city))
print("y not in hyderabad : {}".format('y' not in city))

