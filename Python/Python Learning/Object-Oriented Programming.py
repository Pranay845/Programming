# Topic: Programming paradigms
"""
Python is a multi-paradigm programming language.
It supports different programming approaches.
Programming paradigm is an approach to solve problem using some programming language
or also we can say it is a method to solve a problem using tools and techniques that
are available to us following some approach.
There are lots for programming language that are known
but all of them need to follow some strategy when
they are implemented and this methodology/strategy is paradigms.
"""

# SubTopic: Object-oriented programming
"""
Any object in real life has characteristics.
This is also illustrated in programming languages
One of the popular approaches to solve a programming problem is by creating objects.
This is known as Object-Oriented Programming (OOP).
An object has two characteristics:
    1. attributes
    2. behavior

Let's take an example:
A parrot is an object, as it has the following properties:
    1. name, age, color as attributes
    2. singing, dancing as behavior
    
The concept of OOP in Python focuses on creating reusable code.
This concept is also known as DRY (Don't Repeat Yourself).
"""

# Topic: Class
"""
A class is a blueprint or a design for a object that defines the it's attributes (variables in OOPs) and
the methods (Functions in OOPs) common to all objects or instances  of a same design.
"""

# SubTopic: __init__ method
"""
The __init__ method is a special method which is executed every time automatically
when a object of it's class is created and executed.
This is similar to constructors in other languages.

Constructors are used to initialize or
create attributes/variables in a class for the object and
also these are responsible for the allocation of the object created by the class in the memory.
We can also change the variables inside the class in outside of the class.
These attributes created by the init method can be used inside the class.

In every method of class a argument is passed called self.
self is a pointer to determine based on which object is calling a specific method or referring to what in a class.

These method is useful when you need to create attributes which can be used by other methods in class.
"""

# Note: When we want compare two objects we create a compare function inside the class and pass the two arguments
#  one is which object is calling and the other is which object needs to be compared.
#  The argument need not to be the name of the object which is compared.
#  Then we use if statement and the compare method to compare objects
#  because python does not know how to compare objects.

# SubTopic: Types of attributes (Variables)
"""
There are three different types of variables in OOPs in python:
    1. Instance variable (These variables are created inside the init method with the self keyword.
                          These variables can are different to each object and
                          we can change the variable even outside the class.
                          This is a Object level variable).
                          
    2. Static variable (These variables are directly created under a class as a normal variable.
                        These variables will apply to every object made by the class
                        These cannot be changed outside the class hence the name static (Always the same).
                        This is a Class level variable).

    3. Local variable (These variables are created in a method and only can used inside the method.
                       This is a  Method level variable).
"""

# SubTopic: Types of methods (Functions)
"""
There are Three different types of Methods in OOPs in python:
    1. Instance method (This method is used to work with the object.
                        This method can only be used with a object.
                        In instance methods there are two types of methods:
                            They are accessor methods (These methods are used for accessing the objects attributes) and
                            mutator methods (These are used to manipulate the object's attributes).
                        Instance methods can be used with instance variable. In instance method we use self keyword).
                        
    2. Class method (This method is used to work with class variables.
                     We pass only one argument which is not the self keyword and it's cls.
                     This method can be called with the class name as it is a class method.
                     To tell python, it's a class method we use a built-in decorator called classmethod).
                     
    3. Static method (This has nothing to do with class or instance variables.
                      So, we don't pass any arguments to this method.
                      To tell python, it's a static method we use a built-in decorator called staticmethod.
                      This method works like a simple and a  plain function same like the functions outside the class).
"""

# SubTopic: Magic/Dunder methods
""""""

# Topic: Object
""""""
# SubTopic: Object creation
""""""

# SubTopic: Calling an object's method
""""""

# SubTopic: Using methods
""""""

# SubTopic: Object introspection
""""""

# Topic: Inheritance
""""""

# SubTopic: Types of inheritance
""""""

# Topic: Polymorphism
""""""

# SubTopic: Duck typing
""""""

# SubTopic: Operator overloading
""""""

# SubTopic: Method overloading and overriding
""""""

# Topic: Abstraction
""""""

# SubTopic: Abstract methods and classes
""""""

# Topic: Encapsulation
""""""

# Topic: Methods v/s Functions
""""""

# Topic: Access specifiers
""""""

# Topic: Meta classes
""""""

# SubTopic: Type class
""""""
