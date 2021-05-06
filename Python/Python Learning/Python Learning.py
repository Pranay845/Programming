# Topic: Hello World! Program
"""
Let's start by the Hello World! Program in python.
"""


print('Hello World!')  # print simply means we are telling python show something in a console.

# Note: We are executing this code in IDLE.


# Topic: Variables
"""
Variables are like containers store data,
they have a name to them like boxes
in our home which have something in it
and we keep a label on it.
"""


number = 5

name = 'name'

print(number)
print(name)


# SubTopic: Data Types of Variables
"""
There are types of variables depend upon the data they store,
like in our home we keep food in one box
and oils in another box. These are called as data types.
There are six data types.
They are:
    1. None
    
    2. Numeric:
        1. Integer
        2. Float
        3. Complex
        
    3. Bool:
        1. True
        2. False
    
    4. Python Collections:
        1. List
        2. Tuple
        3. Set
        5. Dictionary
    
    5. String
    
    6. Array

    7. Range (range(start: An integer number specifying at which position to start.,
     stop: An integer number specifying at which position to stop,
     step: An integer number specifying the incrementation.))
"""


a = 5

b = 2.0

c = 1 + 2j

d = True

e = False

f = 'name'

m = range(10)

# Note: There are some advanced data types like bytearray


# SubTopic: Typecasting
"""
Typecasting is like conversion of centimeters to meters.
In variables typecasting is about converting from one data type to another.
This is done by it's corresponding functions like str, int etc.
"""


# integer
n = 100

# float
f = float(n)
print(f)
print(type(f))

# string
s = str(n)
print(s)
print(type(s))


# SubTopic: Swapping Variables
"""
We can swap variables in programming
but it is a bit difficult in other programming
languages in python it is easy to swap variables.
"""


x = 5
y = 10

x, y = y, x
print('x =', x)
print('y =', y)


# SubTopic: Id’s of Variables
"""
In variables the data should be stored.
When the data is stored in computer
it should be identified by the computer 
so every variable has a id different then it's name.
"""


str1 = 'geek'
print(id(str1))

str2 = 'geek'
print(id(str2))


# SubTopic: Rules of Variables
"""
When declaring variables there are some rules to follow.
They are:
    1. A variable name must start with a letter or the underscore character.
    2. A variable name cannot start with a number.
    3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
    4. Variable names are case-sensitive (name, Name and NAME are three different variables).
    5. The keywords (A reserved word that can be understood by a programming language)
       cannot be used naming the variable.
"""

# Topic: Operators
"""
In math operators are symbols for operations on operands like numbers.
In programming they are the same as in math but they do
operations on many operands etc.
"""


x = 15
y = 4
print(x + y)


# SubTopic: How to use operators with variables
"""
We can use operators with variables in many ways
like adding values etc which are stored in variables.
"""


x = 15
y = 4

# Output: x + y = 19
print('x + y =', x + y)

# Output: x - y = 11
print('x - y =', x - y)

# Output: x * y = 60
print('x * y =', x * y)

# Output: x / y = 3.75
print('x / y =', x / y)

# Output: x // y = 3
print('x // y =', x // y)

# Output: x ** y = 50625
print('x ** y =', x ** y)


# Topic: Print Statement
"""
In above code we saw something print.
Let's see what is it actually.
"""

# SubTopic: print()
"""
print is used to show something on console (Where output is shown to us).
It can be manipulated with different ways by using special characters.
"""


print(5)


# SubTopic: \n New Line
"""
\n is a special character which is used to show output in a new line.
"""


print('Hello\nWorld!')


# SubTopic: end=''
"""
end='' is used to show output in the same line with or without a
character after each line.
"""


print('hello', end='')
print('hello')


# SubTopic: Variables and print
"""
In above topics we were not able to see the output.
So we can use print to show our output with variables.
we can also print different data types like a string and a integer
which is stored in a variable.
"""


a = 5
print(a)

b = 2.0
print(b)

c = 1 + 2j
print(c)

d = True
print(d)

e = False
print(e)

f = 'name'
print(f)


# Topic: Strings
"""
Strings are a sequence of characters in single, double and triple quotes ('', "", """""").
"""


a = 'Hello'
print(a)


# SubTopic: String Functions
"""
Functions are like actions on something like changing or checking the value etc.
So then string functions are something which are used to manipulate or check the value of a string.
"""


# len
a = 'Hello, World!'
print(len(a))

# Check String
txt = 'The best things in life are free!'
print('free' in txt)

# Check if NOT
txt = 'The best things in life are free!'
print('expensive' not in txt)

# Accessing string characters in Python
string = 'programmer'
print('str = ', string)

# first character
print('str[0] = ', string[0])

# last character
print('str[-1] = ', string[-1])

# slicing 2nd to 5th character
print('str[1:5] = ', string[1:5])

# slicing 6th to 2nd last character
print('str[5:-2] = ', string[5:-2])


# SubTopic: f Strings
"""
If we want show variables in between strings we use f strings.
These are special type of string to show variables with strings.
"""


val = 'Geeks'
print(f'{val}for{val} is a portal for {val}.')

name = 'name'
age = 23
print(f'Hello, My name is {name} and I\'m {age} years old.')


# SubTopic: Doc Strings
"""
Doc strings are another special type of string which is written in triple quotes for documentation.
These are also called as multi line comments.
"""


a = """Lorem ipsum 
dolor sit amet"""
print(a)


# SubTopic: Raw Strings
"""
Raw strings are also a special type of string used to show raw format of a string like
if we keep a special character in between a string then to skip it we use raw strings.
"""


s = r'Hi\nHello'
print(s)


# SubTopic: Single, Double, Triple quotes
"""
Single quotes are widely because of comfort. These is mostly used by programmers.
Double quotes are used when there is a single quote in between a string but we can also use it in case of single quotes.
Triple quotes are for writing doc strings or if there is single and double quotes in a string.
"""


# Single Quotes
a = 'Hello'
print(a)

# Double Quotes
a = "Hello"
print(a)

# Triple Quotes
a = """Hello"""
print(a)


# Topic: Inputs
"""
When we need to interact with a user we take inputs.
Inputs are values given or taken by a user.
By default inputs come in a string format
but we can change the data type by typecasting.
"""


val = input('Enter your value: ')
print(val)

num = input('Enter number :')
print(num)
name1 = input('Enter name : ')
print(name1)

# Printing type of input value
print('type of number', type(num))
print('type of name', type(name1))


# Topic: More on Operators
"""
We will see more about operators.
"""

# SubTopic: Types of Operators
"""
There are different types of operators.
They are:
    1. Arithmetic Operators
    2. Relational Operators
    3. Logical Operators
    4. Unary Operator
    5. Bitwise Operators
    6. Assignment Operators
    7. Special Operators
"""

# SubTopic: Arithmetic Operators
"""
Arithmetic operators are used to perform mathematical operations.
Types of arithmetic operators:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Floor Division (// (Returns the integral part of the quotient.))
    6. Modulus (% (Returns the reminder of division))
    7. Exponent (**)
"""


x = 15
y = 4

# Output: x + y = 19
print('x + y =', x + y)

# Output: x - y = 11
print('x - y =', x - y)

# Output: x * y = 60
print('x * y =', x * y)

# Output: x / y = 3.75
print('x / y =', x / y)

# Output: x // y = 3
print('x // y =', x // y)

# Output: x ** y = 3
print('x ** y =', x % y)

# Output: x ** y = 50625
print('x ** y =', x ** y)


# SubTopic: Relational Operators
"""
Relational operators compares the values.
It either returns true or false according to the condition.
Types of relational operators:
    1. Greater Than (>)
    2. Less Than (<)
    3. Equal To (==)
    4. Not equal to (!=)
    5. Greater than or equal to (>=)
    6. Less than or equal to (<=)
"""


x = 10
y = 12

# Output: x > y is False
print('x > y is', x > y)

# Output: x < y is True
print('x < y is', x < y)

# Output: x == y is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)


# SubTopic: Logical Operators
"""
Logical operators perform Logical operations like checking true or false.
Types of logical operators:
    1. Logical AND (and: True if both the operands are true)
    2. Logical OR (or: True if either of the operands is true)
    3. Logical NOT (not: True if operand is false (complements the operand))
"""


x = True
y = False

print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)


# SubTopic: Unary Operator
"""
Unary operator is to fetch a negative value of a number.
"""


p = 9
print(-p)


# SubTopic: Bitwise Operators
"""
Bitwise operators are operators which do operations on bits.
Types of bitwise operators:
    1. Bitwise AND (&: Sets each bit to 1 if both bits are 1)
    2. Bitwise OR (|: Sets each bit to 1 if one of two bits is 1)
    3. Bitwise NOT (~: Inverts all the bits)
    4. Bitwise XOR (^: Sets each bit to 1 if only one of two bits is 1)
    5. Bitwise Left Shift (<<: Shift left by pushing zeros in from the right and let the leftmost bits fall off)
    6. Bitwise Right Shift (>>: Shift right by pushing copies of the leftmost bit in from the left,
                            and let the rightmost bits fall off)
"""


a = 10
b = 4

# bitwise AND
print('a & b =', a & b)

# bitwise OR
print('a | b =', a | b)

# bitwise NOT
print('~a =', ~a)

# bitwise XOR
print('a ^ b =', a ^ b)

a = 10
b = -10

# bitwise right shift
print('a >> 1 =', a >> 1)
print('b >> 1 =', b >> 1)

a = 5
b = -10

# bitwise left shift
print('a << 1 =', a << 1)
print('b << 1 =', b << 1)


# SubTopic: Assignment Operators
"""
Assignment operators are used to assign values to the variables.
Types of Assignment operators:
    1. Assign (=)
    2. Add and Assign (+=)
    3. Subtract and Assign (-=)
    4. Multiply and Assign (*=)
    5. Divide and Assign (/=)
    6. Modulus and Assign (%=)
    7. Floor divide and Assign (//=)
    8. Exponent and Assign (**=)
    9. Bitwise AND and Assign (&=)
    10. Bitwise OR and Assign (|=)
    11. Bitwise XOR and Assign (^=)
    12. Bitwise Left Shift and Assign (>>=)
    13. Bitwise Right Shift and Assign (<<=)
"""


x = 5  # x = 5
print(x),

x += 5  # x = x + 5
print(x)

x -= 5  # x = x - 5
print(x)

x *= 5  # x = x * 5
print(x)

x /= 5  # x = x / 5
print(x)

x %= 5  # x = x % 5
print(x)

x //= 5  # x = x // 5
print(x)

x **= 5  # x = x ** 5
print(x)

x &= 5  # x = x & 5
print(x)

x |= 5  # x = x | 5
print(x)

x ^= 5  # x = x ^ 5
print(x)

x >>= 5  # x = x >> 5
print(x)

x <<= 5  # x = x << 5
print(x)


# SubTopic: Special Operators
"""
Types of special operators:
    1. Identity operators
        1. is
        2. is not

    2. Membership operators
        1. in
        2. not in
"""


# Identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

# Membership operators
x = 'Hello world'
y = {1: 'a', 2: 'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)


# SubTopic: Numeric Conversion
"""
In python there are four types of number system.
They are:
    1. Decimal (Base 10, 0-9)
    2. Octal (Base 8, 0-7, prefix: 0o)
    3. Hexadecimal (Base 16, 0-7 a-f, prefix: 0x)
    4. Binary (Base 2, 0-1, prefix: 0b)

There are different functions to convert a number from one system to another.
"""


# Octal (Base 8, 0-7)
oct(25)

# Hexadecimal (Base 16, 0-7 a-f)
hex(23)

# Binary (Base 2, 0-1)
bin(23)


# SubTopic: Errors of Operators
"""
When dealing operators we can get errors in code.
Many errors come because we might perform operations on different
data types like a number with a string.
"""


# v = 'hello' + 5
# print(v)

# Note: This code does not work


# Topic: Decision Control Flow
"""
Decision Control flow means that controlling the flow or deciding of execution of a program.
To control the flow in python we use if, elif, else keywords or blocks.
In python we call them as Suite. We also to follow some rules when the code.
In programming languages it is called as Syntax.
"""

# SubTopic: If
"""
if is a keyword used for determining whether a condition is true or false.
If the condition is true then only it shall execute the following statements.
"""


a = 33
b = 200
if b > a:
    print('b is greater than a')


# SubTopic: If, Else
"""
else is another keyword which tells python to try this condition
if the previous condition was false.
"""


a = 200
b = 33
if b > a:
    print('b is greater than a')
else:
    print('a is greater than b')


# SubTopic: If, Elif, Else
"""
elif is also another keyword which tells python to try this condition
if the previous if condition is false.
We can use as many as if's, elif's or else we want but they should follow a order of if, elif, else.
"""


a = 200
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')


# SubTopic: Nested If Statements
"""
When we have if, elif, else inside if or elif or else than these are called as nested statements.
We can use them randomly with following the order.
We can also be make infinite nested statements.
We can also make infinite if, elif, else
"""


num = float(input('Enter a number: '))
if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('Positive number')
else:
    print('Negative number')


# Topic: Repetition Control Flow
"""
When want to perform a task repeatedly then we use loops.
These is called as repetition control flow.
There are two types of loops.
They are:
    1. for loop
    2. while loop
"""

# SubTopic: for Loop
"""
for loop is for iterating (repeating a operation) a sequence like a string etc.
With for loop we can execute many operations for each value in a sequence.
"""


for i in range(10):
    print(i)


# SubTopic: for, else
"""
We can use for, else together in python in some scenarios like iterating a sequence to check a condition
and if it is not true then do another operation only once.
"""


for x in range(6):
    print(x)
else:
    print('Finally finished!')


# SubTopic: while Loop
"""
while loop will execute a block of statements repeatedly until the condition is true.
If the condition becomes false it will stop.
"""


"""
Program to add natural
numbers up to
sum = 1+2+3+...+n
"""

# To take input from the user,
# n = int(input('Enter n: '))

n = 10

# initialize sum and counter
sums = 0
i = 1

while i <= n:
    sums = sums + i
    i = i + 1  # update counter

# print the sum
print('The sum is', sums)


counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')


# SubTopic: Nested Loops
"""
When there is a loop inside a loop (Irrespective of which loop it is) is called as nested loops.
These nested loops can both while and for loops together.
We can also be make infinite nested loops.
"""


for x in range(10):
    for i in range(10):
        print(i)


# SubTopic: Range
"""
Range is a function used for ranging (start to end) numbers.
It can be used separately without a loop.
"""

# SubTopic: break, continue, pass
"""
break, continue, pass are keywords used mainly in loops.
1. break means stop the loop.
2. continue means leave this iteration and go to the next iteration.
3. pass means there are no statements here, skip it. pass can also be used with if, elif, else statements.
"""


# break
"""
Use of break statement inside the loop
"""

for val in 'string':
    if val == 'i':
        break
    print(val)

print('The end')

# continue
"""
Program to show the use of continue statement inside loops
"""

for val in 'string':
    if val == 'i':
        continue
    print(val)

print('The end')

# pass
"""
pass is just a placeholder for
functionality to be added later.
"""

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass


# Topic: Python collections
"""
Collections are a set of values which can be stored at once.
These are also called as container types.
There are four types of collections.
They are:
    1. List ( [] )
    2. Tuple ( () )
    3. Set ( {} )
    4. Dictionary ( { : } )
"""

# SubTopic: List
"""
List is a collection of values written inside square brackets ( [] ) separated by commas ( , ).
It can store duplicate values.
It can store different data types like string, bool etc.
It can also store any python collections including list.
It is mutable (After making it we can change it).
It is iterable.
"""


thislist = ['apple', 'banana', 'cherry']
print(thislist)

thislist = ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(thislist)

list1 = ['apple', 'banana', 'cherry']
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ['abc', 34, True, 40, 'male']


# SubTopic: Functions of List
"""
There are many functions of list like append, pop etc.
These functions can only used on lists and some of them can be used on any data types.
"""


# len
cars = ['Ford', 'BMW', 'Volvo']
len(cars)

# append
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')

# clear
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

# extend
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

# pop
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

# insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')

# sort
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()


# SubTopic: List Comprehension
"""
When we need to iterate a list
we will make a list or take input
and make a for or while loop and add if statements
but we have a elegant way to do this.
We can make a for or while loop with if statements inside a list.
This is called as list comprehension.
"""


# Without list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)

# With list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = [x for x in fruits if 'a' in x]
print(newlist)

# Note: syntax: newlist = [expression for item in iterable if condition == True]


# SubTopic: Tuple
"""
Tuple is also a collection of values written inside parenthesis ( () ) separated by commas ( , )
but unlike lists tuple is immutable (After making it we cannot change it)
because of immutability there is no tuple comprehension.
In other ways tuple is quite similar to list.
"""


mytuple = ('apple', 'banana', 'cherry')

thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

thistuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple)

thistuple = ('apple',)
print(type(thistuple))

# NOT a tuple
thistuple = ('apple')
print(type(thistuple))


# SubTopic: Functions of Tuple
"""
There are many functions of tuple.
Because tuple is immutable there fewer functions like append
compared to other data types.
"""


# count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)


# SubTopic: Set
"""
Set is a collection of values written inside curly brackets ( {} ) separated by commas ( , )
but unlike lists set only stores unique values and it is unordered
because it is unordered we cannot access items using indexes in it.
We use sets in some scenarios instead of list because set is highly optimized method
for checking whether a specific element is present.
"""


myset = {'apple', 'banana', 'cherry'}

thisset = {'apple', 'banana', 'cherry'}
print(thisset)

# Note: Sets are unordered,
#  so you cannot be sure in which order the items will appear.

thisset = {'apple', 'banana', 'cherry', 'apple'}
print(thisset)

# Note: Duplicate values will be ignored


# SubTopic: Functions of Set
"""
There are many functions in set.
Because set is unordered there fewer functions like index
compared to other data types.
"""


# add
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)

# clear
fruits = {'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)

# difference
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.difference(y)
print(z)

# intersection
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
z = x.intersection(y)
print(z)

# pop
fruits = {'apple', 'banana', 'cherry'}
fruits.pop()
print(fruits)

# remove
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('banana')
print(fruits)

# update
x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}
x.update(y)
print(x)


# SubTopic: Set Comprehension
"""
Like list comprehensions we also have set comprehensions
but result would be unordered because it is a set.
"""


# Without set comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
output_set = set()

# Using loop for constructing output set
for var in input_list:
    if var % 2 == 0:
        output_set.add(var)

print('Output Set using for loop:', output_set)

# With Set comprehensions
# for constructing output set
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set_using_comp = {var for var in input_list if var % 2 == 0}
print('Output Set using set comprehensions:', set_using_comp)


# SubTopic: Dictionary
"""
Dictionary is a collection of values written inside square brackets ( {} )
in a key, value pair separated by comma ( , ).
Key and Value are separated by colan ( : ).
It holds a pair of values,
one being the key (These are case sensitive)
and the other corresponding pair element being its value.
Values in a dictionary can be of any data type and can be duplicated,
whereas keys can’t be repeated and must be immutable.
It is also called as mapping type because we map values to keys.
It is like a mixture of set and list with key, value pair
"""


thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict)

# Note:As of Python version 3.7, dictionaries are ordered.
#  In Python 3.6 and earlier, dictionaries are unordered.

# Dictionary Items
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict['brand'])

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964,
#     'year': 2020
# }
# print(thisdict)

# Note: Duplicate values will overwrite existing values


# SubTopic: Functions of Dictionary
"""
There are many functions in dictionary.
Because dictionary is mapping type there few extra functions like keys
compared to other data types.
"""


# len
print(len(thisdict))

# clear
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car.clear()
print(car)

# fromkeys
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# get
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.get('model')
print(x)

# items
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.items()
print(x)

# pop
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
car.pop('model')
print(car)

# values
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.values()
print(x)


# Subtopic: Nested Dictionaries
"""
A dictionary can contain dictionaries,
this is called nested dictionaries.
"""


myfamily = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2': {
        'name': 'Tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}


# SubTopic: Dictionary Comprehension
"""
Like set comprehension we also have dictionary comprehension
but it is quite different then set comprehension because of key, value pair.
"""


# Dictionary comprehension

# Lists to represent keys and values
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# but this line shows dict comprehension here
myDict = {k: v for (k, v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print(myDict)


# Topic: Typecasting in Collections
""" 
We can change a collection to another collection
by it's corresponding functions like list, dict.
We can also make a collection without using
it's specified brackets by using it's corresponding
keyword like list, dict etc.
"""


# We are converting a list into a tuple
s = [1, 2, 3, 4, 5, 6]
s = tuple(s)


# Topic: Functions
"""
Let us see what functions are exactly are.
Functions are set of statements to achieve a specific task like adding numbers etc.
We use functions because it is reusable instead of writing or copy pasting the code.
In python we have so many in-built functions like print, input etc.
They are like helpers.
Functions have two steps.
They are:
    1. Defining a function
    2. Calling a function
"""


# Defining a function
def greet():
    print('Hello, Good morning!')


# Calling a function
greet()


# SubTopic: Types of Functions
"""
There are two types of functions.
They are:
    1. Built-in functions (Like len())
    2. User-defined functions (Functions that we make)
"""

# SubTopic: Parameters (Arguments)
"""
Parameter are special kind of variable passed to a function to
perform a specific task on those variables.
When the input is given to a function it is called as a argument.
There are different types of parameters.
"""


# This function expects 2 arguments, and gets 2 arguments

def my_function(fname, lname):
    print(fname + ' ' + lname)


my_function('Emil', 'Refines')


# SubTopic: Pass by Value or Reference
"""
Pass by value means we are passing the value of the variable
not the variable itself so it would use a different memory location.
Pass by reference means we are passing the address or memory location of the variable
by these the variable will changed inside and outside the function.
In python we have a different concept that
if we access the variable then the memory location would be same
but when we change the value inside the function it will take another memory location
so it would not affect the outside variable because the value is immutable
if the value is mutable it will change the variable outside the function also.
"""


def set_list(list):
    list = ['A', 'B', 'C']
    return list


def add(list):
    list.append('D')
    return list


my_list = ['E']

print(set_list(my_list))
print(add(my_list))


# SubTopic: Types of Parameters
"""
There are four types of parameters.
They are:
    1. Positional
    2. Keyword
    3. Default
    4. *args and **kwargs (*args: The syntax is to use the symbol * to take in a variable number of arguments;
                           by convention, it is often used with the word args.
                           What *args allows you to do is take in more arguments than the number of formal arguments 
                           that you previously defined. With *args, any number of extra arguments can be tacked on to 
                           your current formal parameters (including zero extra arguments).
                           
                           **kwargs: The special syntax **kwargs in function definitions in python is used to 
                           pass a keyworded, variable-length argument list.
                           We use the name kwargs with the double star.
                           The reason is because the double star allows us to
                           pass through keyword arguments (and any number of them).)



A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
That is why when we iterate over the kwargs there doesn't seem to be any order in which they were printed out.)
    
Normally if we make a function then all the parameters should be specified
but we can make parameters optional or not compulsory by many ways.
These are called as optional parameters.
"""


# Positional
def adding(o, ab, q):
    return (o + ab + q)


adding(1, 2, 3)


# Keyword
def greet(human, msg):
    print('Hello', name + ', ' + msg)


greet(msg='How do you do?', human='Bruce')


# Default
def adding(w, r=5, t=10):
    return (w + r + t)


adding(1, 2, 3)


# *args
def myfun(arg1, *argv):
    print('First argument :', arg1)
    for arg in argv:
        print('Next argument through *argv :', arg)


myfun('Hello', 'Welcome', 'to', 'Geeks for Geeks')


# **kwargs
def myfun(**kwargs):
    for key, value in kwargs.items():
        print(f'({key} == {value})')


myfun(first='Geeks', mid='for', last='Geeks')


# SubTopic: Scope of Variables
"""
Normally we make variables inside a function and also outside a function.
This is were Scope comes into play
if we make the same variables inside and outside a function
so then the outside one is called as a global variable which can accessed from anywhere in a file
the inside one is called as local variable which can be accessed only inside that particular function.
To use a global variable inside a function we use the keyword called as global.
"""


# This function has a variable with
# name same as s.
def f():
    me = 'abc'
    print(s)


# Global scope
me = 'I love Geeks for geeks'
f()
print(s)

# scope of variable
a = 1


# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)


# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)


# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


# SubTopic: Lambda Functions
"""
Lambda functions are anonymous functions which means they have no name to them.
Normally when we make functions we should call them after making them
but in lambdas they can be used anywhere.
These are defined in one line so it is also called as one-liner functions.
"""


gh = lambda a: a + 10
print(gh(5))

gh = lambda a, b: a * b
print(gh(5, 6))


# showing difference between def and lambda
def cube(y):
    return y * y * y


lambda_cube = lambda y: y * y * y

# using the normally
# defined function
print(cube(5))

# using the lambda function
print(lambda_cube(5))


# SubTopic: map, filter, reduce
"""
map, filter, reduce are some methods will can be used with lambdas and without it.
These are methods used very commonly in programs.
"""


# map with lambda
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x * 2, li))
print(final_list)

# filter with lambda
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

# reduce with lambda
# to get sum of a list

from functools import reduce

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)


# SubTopic: Recursion
"""
Recursion is about calling the function inside the function.
We can also call different functions inside a function.
Recursion is used in many scenarios.
In some scenarios it makes more sense to use recursion over iteration.
"""


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 3
print('The factorial of', num, 'is', factorial(num))


# SubTopic: Decorator
"""
Decorator is a tool used to modify a function with help of another function
without permanently changing the original function.
It is simply another function which can wrapped on any function
to extend it's behaviour (The task a function does).
We can achieve decorators in few ways.
"""


# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case 'func'
    def inner1():
        print('Hello, this is before function execution')

        # calling the actual function now
        # inside the wrapper function.
        func()

        print('This is after function execution')

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print('This is inside the function !!')


# SubTopic: Generators
"""
Generators are functions with yield keyword instead of return keyword.
yield is used to generate a value at a time.
It is used in some scenarios like handling large datasets where we will work only on a single dataset.
"""


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFun():
    print(value)


# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
print(x.next())  # In Python 3, __next__()
print(x.next())
print(x.next())
print(x.next())
print(x.next())

# Iterating over the generator object using for
# in loop.
print('\nUsing for in loop')
for i in fib(5):
    print(i)


# Topic: Modular Programming
"""
Modular programming is a way to write code and organize it.
This is very useful for maintenance of code and many other benefits.
Many companies use modular programming to write code because of it's benefits.
"""

# SubTopic: Modules
"""
Modules are simply python files arranged and written code
in such a way like functions in one file, variables in one file etc.
These modules can also be reused.
There are also built-in modules.
"""

# SubTopic: import
"""
import is a keyword used to bring in other modules
into a python file or a module.
These is mainly used to import built-in modules.
"""


import math


# SubTopic: from
"""
from is also a keyword used before import keyword to
import a specific part of a module like a function etc.
"""


from math import sqrt


# SubTopic: Packages
"""
Packages are a collection of modules which are also called as library.
Packages are simply a directory of python files with init.py file.
init.py is there to tell python this directory as a package.
"""

# SubTopic: Types of Modules
"""
There are two types of modules.
They are:
1. Built-in modules
2. Created modules
"""

# SubTopic: Created Modules
"""
Created modules are modules which we create by ourself.
Any python file is called a module.
Mostly modules have code which should imported
that means it does not have runnable code also called as a script.
"""

# SubTopic: Pip
"""
Pip stands for pip install package.
It is a package manager which is bundled with python.
It is used for installing third-party modules or packages
created by other developers which help us for various purposes.
"""

# SubTopic: Module Installation
"""
To install a module:
1. We open the terminal or powershell
2. Type the command pip install <package name>
"""

# SubTopic: Virtual Environment (venv)
"""
Virtual Environment is a like a isolated folder or project which has a separate python
than the system-wide python by this we can install packages for only the separate python.
When we have multiple projects with different sets of dependencies or requirements
we can make different Virtual Environments for different projects.
"""

# SubTopic: What modules contain?
"""
Modules contain different sets of statements like functions and variables etc.
They are made in mind that these would be imported to other files so usually they don't runnable code.
"""

# SubTopic: Module v/s Script
"""
Module is a python file which is usually imported to other files.
Script is a runnable code like adding two numbers etc.
But modules can also have runnable code.
"""

# SubTopic: Special Variable __name__
"""
A special variable __name__ is to determine
whether a module is the main module or not.
"""


# File1.py

print(f'File1 __name__ = {__name__}')

if __name__ == '__main__':
    print('File1 is being run directly')
else:
    print('File1 is being imported')

# File2.py

# import File1

print(f'File2 __name__ =  {__name__}')

if __name__ == '__main__':
    print('File2 is being run directly')
else:
    print('File2 is being imported')


# Topic: Math Module
"""
Math module is used for doing advanced calculations
which are not built-in to python directly like sqrt,factorial etc.
"""

# Topic: Array
"""
Array is also a python collection like list,set and tuple etc.
But it is a bit more complex than others.
"""


# importing 'array' for array creations
import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])

# printing original array
print('The new created array is : ', end=' ')
for i in range(0, 3):
    print(a[i], end=' ')
print()

# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# printing original array
print('The new created array is : ', end=' ')
for i in range(0, 3):
    print(b[i], end=' ')

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
#  However, to work with arrays in Python you will have to import a library, like the NumPy library.


# SubTopic: Functions of array
"""
There are many functions of array like typecode, itemsize etc.
These functions can only used on arrays and some of them can be used also on any data types.
"""


# array with int type
a = arr.array('i', [1, 2, 3, 4, 5, 6])

# accessing element of array
print('Access element is: ', a[0])

# accessing another element of array
print('Access element is: ', a[3])

# array with float type
b = arr.array('d', [2.5, 3.2, 3.3])

# accessing element of array
print('Access element is: ', b[1])

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Initial Array: ')
for i in (a):
    print(i, end=' ')

# Print elements of a range
# using Slice operation
Sliced_array = a[3:8]
print('\nSlicing elements in a range 3-8: ')
print(Sliced_array)

# Print elements from a
# pre-defined point to end
Sliced_array = a[5:]
print('\nElements sliced from 5th '
      'element till the end: ')
print(Sliced_array)

# Printing elements from
# beginning till end
Sliced_array = a[:]
print('\nPrinting all elements using slice operation: ')
print(Sliced_array)

funarray = arr.itemsize()
print(funarray)

funarrays = arr.typecode()
print(funarrays)


# SubTopic: Numpy Library
"""
To use arrays more comfortably and effectivity we use numpy (A Library).
Numpy is a third-party library so, we need to install it through pip.
It has some good features and implementations.
"""

import numpy as np

# SubTopic: Multi Dimensional Array
"""
With numpy we can make a multi-dimensional array
most likely a two-dimensional array.
Two-Dimensional Array consists of various rows and columns like a matrix.
"""


# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# type
print('Array is of type: ', type(arr))

# ndim
print('No. of dimensions: ', arr.ndim)

# shape
print('Shape of array: ', arr.shape)

# size
print('Size of array: ', arr.size)

# dtype
print('Array stores elements of type: ', arr.dtype)

# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, ::2]
print('Array with first 2 rows and alternate'
      'columns(0 and 2):\n', temp)

# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print('\nElements at indices (0, 3), (1, 2), (2, 1),'
      '(3, 0):\n', temp)

# boolean array indexing example
cond = arr > 0  # cond is a boolean array
temp = arr[cond]
print('\nElements greater than 0:\n', temp)


# Topic: Exception or Error handling
"""
Errors are the problems in a program
due to which the program will stop the execution.
So exceptions are raised when the program is syntactically correct
but the code resulted in an error.
This exception does not stop the execution of the program,
however, it changes the flow of the program.
"""

# SubTopic: Types of Errors
"""
There are three types of errors.
They are:
1. Syntax Errors
2. Logical Errors
3. Runtime Errors

Syntax Errors are done by the developer with syntax.
Logical Errors are which have problem with the logic.
Runtime Errors are which user make so as a developer
we need to handle those errors.
We can to it in python by using try, except keywords.
"""

# SubTopic: try, except, finally
"""
try is a keyword which is used before the
problematic or questionable statements in logic and runtime.
except keyword is used to manipulate the error.
finally is used to complete the error like closing a file.
"""


a = [1, 2, 3]

try:
    print(f'Second element = {(a[1])}')

    # Throws error since there are only 3 elements in array
    print(f'Fourth element = {(a[3])}')

except IndexError:
    print('An error occurred')

# No exception Exception raised in try block
try:
    k = 5 // 0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print('Can\'t divide by zero')

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')


# SubTopic: Raising Exceptions
"""
Sometimes we know a error can occur so we raise exceptions to handle it
in such a way that user could understand like popping a message etc.
"""


x = -1

if x < 0:
    raise Exception('Sorry, no numbers below zero')

x = 'hello'

if not type(x) is int:
    raise TypeError('Only integers are allowed')


# Topic: File I/O
"""
In python we can play with files like .txt, .pdf files etc.
We can edit and read files.
First we need to open a file, play with it and close the file.
There are four types of modes to open a file.
They are:
1. "r" for reading.
2. "w" for writing.
3. "a" for appending.
4. "r+" for both reading and writing
We can also create files.
"""

# SubTopic: Directories
"""
Directories are important because
when you create a file it will be created in the working directory.
When you try to open a file it will search in the working directory
until we specify the file path.
We can also create in different directories.
"""

# SubTopic: open keyword
"""
open keyword is used to open a file.
It is mandatory to open the file before you work with it.
"""


# a file named 'Python Learning',
# will be opened with the reading mode.
file = open('Python Learning.txt', 'r')

# This will print every line one by one in the file
for each in file:
    print(each)

# read
file = open('Python Learning.txt', 'r')
print(file.read())

# read with characters
file = open('Python Learning.txt', 'r')
print(file.read(5))


# SubTopic: open, close
"""
After you open the file and work with it,
it is a good practice to close the file.
To close a file we use the close keyword.
"""


# create a file
file = open('Python Learning.txt', 'w')
file.write('This is the write command')
file.write('It allows us to write in a particular file')
file.close()

# append
file = open('Python Learning.txt', 'a')
file.write('This will add this line')
file.close()


# SubTopic: with Keyword
"""
With the help of with suite (A group of individual statements which make a code block like if, for, while
and also with keywords. All suites require indentation. Suite is also called as block)
we no longer need to close the file because with block will close it by itself.
It is a good practice to use with suite to work with files.
"""


# with
with open('Python Learning.txt') as file:
    data = file.read()

# with along with write
with open('Python Learning.txt', 'w') as f:
    f.write('Hello World!!!')

# split
with open('Python Learning.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


# Documentation: https://docs.python.org/3/
