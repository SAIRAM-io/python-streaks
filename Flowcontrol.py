
''' CONDITIONAL STATEMENTS'''
# if
num = 10
if (num == 10):
	print("True")

# if - else
num = -20
if (num > 0):
	print("Positive number")
else:
	print("Negative number")

# if - elif - else
num = 0
if num > 0:
	print("Positive number")
elif num < 0:
	print("Negative number")
else:
	print("Zero")


''' LOOPING STATEMENTS'''
# for loop
for i in range(10):
	print(i)

for i in range(2, 10):
	print(i)

for i in range(10, 30, 3):
	print(i)

for i in "Hello World!!":
	print(i)

# while
num = 1
while num <= 10:
	print(num)
	num += 1

''' FLOW CONTROL '''
# BREAK
num = 1
while True:
	if num is 5:
		break
	else:
		print(num)
	num += 1

# CONTINUE
for i in "banana":
	if i == 'a':
		continue
	else:
		print(i)

# PASS
is_logged_in = True
if (is_logged_in):
	pass
else:
	pass