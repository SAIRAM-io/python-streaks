'''
    Object-oriented programming is a programming paradigm based on the concept of "objects",
    Ths is all about creating objects that contain both data(properties) and functions(methods).

    Class is a blueprint or template from which objects are created.
    Object is an instance of a class.

    Class is a group of similar objects.
    Object is a real world entity

    Object is a physical entity.
    Class is a logical entity.

    Object allocates memory when it is created. 
    Class doesn't allocated memory when it is created.
'''

# we define class using 'class' keyword. And we create objects using classname()
# we access attributes & methods using 'object_name.property_name', 'object_name.method_name'
class class_name:
    """docstring for class_name"""
    # we define attributes (properties)
    # we define methods (functions)
obj = class_name()


# Example:
class Animal:
#   Attributes -- defines properties
    name = 'Lion'
    weight = 78
    
#   Methods -- defines functionalities
    def eat(self):
        print('Lion is eating...')
    def chase(self):
        print('Lion is chasing...')

lion = Animal()         # creating object
print(lion.name)        
print(lion.weight)
lion.eat()
lion.chase()


# SELF: The self is used to represent the instance of the class.
# It binds a specific object to the class
class Employee:
    def declare_employee(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(self.name, self.salary)

# 1st object
harsh = Employee()
harsh.declare_employee('Harsh', 35000)
harsh.show()
# 2nd object
chaitan = Employee()
chaitan.declare_employee('Chaitan', 40000)
chaitan.show()


# Constructor is a special metyhod which is called automatically when object is created
# The task of constructors is to initialize(assign values) to the properties.
# def __init__() is a constructor
class Employee:
    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(self.name, self.salary)
        
harsh = Employee('Harsh', 35000)
harsh.show()

chaitan = Employee('Chaitan', 40000)
chaitan.show()

# another example
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')

num1 = ComplexNumber(2, 3)


# class attributes and Instance attributes
# Class attributes -- Can be accesed by every object (Equal for every object)
                        # using class_name.attribute
# Instance attributes -- Can be accesed by its own instance (object)
                        # using obj_name.attribute
class Employee:
    # class attribute
    manager_name = 'Jack'
    
    def __init__(self, name, salary):
        # instance attributes
        self.name = name
        self.salary = salary
    def show(self):
        print(self.name, self.salary)
        
harsh = Employee('Harsh', 35000)
harsh.show()

chaitan = Employee('Chaitan', 40000)
chaitan.show()

print('Manager name:', Employee.manager_name)

# Inheritance
# Inheritance is a way of creating a new class for using details of an existing 
# class without modifying it. The newly formed class is a derived class (or child class). 
# Similarly, the existing class is a base class (or parent class).
class Shape:
    def __init__(self, no_of_sides):
        self.sides = no_of_sides
        self.length_sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.length_sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.sides)]

    def show_sides(self):
        for i in range(self.sides):
            print("Legth of side {} : {}".format(i+1, self.length_sides[i]))

class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self, 3)

    def findArea(self):
        a, b, c = self.length_sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of Triangle : {:.2f}'.format(area))

class Square(Shape):
    def __init__(self):
        super().__init__(self, 1)

    def findArea(self):
        area = 4*self.length_sides[0]
        print('The area of Square : {:.2f}'.format(area))

t1 = Triangle()
t1.input_sides()
t1.show_sides()
t1.findArea()

s1 = Square()
s1.input_sides()
s1.show_sides()
s1.findArea()

# checks whether the object belongs to the class specified or not
print(isinstance(s1, Square))
print(isinstance(s1, Shape))
print(isinstance(s1, Triangle))
print(isinstance(s1, object))

# Another example
class Shape:
    def __init__(self, shape_name):
        if shape_name == 'square':
            self.no_sides = 1
        elif shape_name == 'rectangle':
            self.no_sides = 2
        elif shape_name == 'triange':
            self.no_sides = 3

    def take_input(self):
        self.sides = []
        print(f'Enter {self.no_sides} sides: ')
        for i in range(self.no_sides):
            self.sides.append(int(input()))

class Square(Shape):
    def __init__(self):
        super().__init__('square')
        super().take_input()
    def area(self):
        print(f'Area of Square: {self.sides[0]**2}')

class Rectangle(Shape):
    def __init__(self):
        super().__init__('rectangle')
        super().take_input()
    def area(self):
        print(f'Area of Rectangle: {self.sides[0]*self.sides[1]}')

class Triangle(Shape):
    def __init__():
        super().__init__('triange')
    def area():
        pass

sq = Square()
sq.area()

rec = Rectangle()
rec.area()

# Multiple Inheritance
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

# Multilevel Inheritance
class GrandParent:
    pass

class Parent(GrandParent):
    pass

class Child(Parent):
    pass


# Method Overloading -- Python wont support Method Overloading as it is dynamically typed language.

# Method overiding
class Sample:
    def __init__(self):
        pass
    def show(self):
        print('sample class')

class Child(Sample):
    def __init__(self):
        pass
    def show(self):
        # super().show()
        print('child class')

a = Child()
a.show()

# Access Specifiers:

# Public Access Specifier: accessed from outside the class and also by other classes too
class ClassA():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def show(self):
        print(self.a, self.b)

obj_a = ClassA(10, 20)
print(obj_a.a, obj_a.b)
obj_a.show()

# Private Access Specifier: only accessible within the class. (__variable)
class ClassA():
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def show(self):
        print(self.__a, self.__b)

obj_a = ClassA(10, 20)
print(obj_a.__a, obj_a.__b)         # throws an error
obj_a.show()

# There is a way to access private attributes
print(obj_a._ClassA__a, obj_a._ClassA__b)

# Protectyed Access Specifier: accessible from within the class and are also available to its sub-classes (_variablename)
# We can still access these attributes. The responsible programmer would refrain from accessing and modifying instance these attibutes

class ClassA():
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def show(self):
        print(self._a, self._b)

obj_a = ClassA(10, 20)
print(obj_a._a, obj_a._b)
obj_a.show()
