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

# SubTopic: Object-Oriented Programming
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

# SubTopic: __init__ Method
"""
The __init__ method is a special method which is executed every time automatically
when a object of it's class is created and executed.
This is similar to constructors in other languages.

Constructors are used to initialize or
create attributes/variables in a class and the creation of the object and
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

# SubTopic: Types of Attributes (Variables)
"""
There are three different types of variables in OOPs:
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

# SubTopic: Types of Methods (Functions)
"""
There are Three different types of Methods in OOPs:
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

# SubTopic: Magic/Dunder Methods
"""
Dunder or magic methods in Python are the methods having
two prefix and suffix underscores in the method name.
Dunder here means “Double Under (Underscores)”.
Few examples for magic methods are:
1. __init__
2. __add__
3. __len__
4. __repr__ etc.
"""

# SubTopic: Inner Class
"""
Inner class is a class made inside a another class.
This is possible because executes line by line.
To access the inner class we need to first write outer class than the inner class and
then we can access the inner class.
"""

# Topic: Object
"""
An Object is an instance of a Class.
A class is like a blueprint while an instance
is a copy of the class with actual values.
An object consists of:
1. State: It is represented by the attributes of an object.
2. Behavior: It is represented by the methods of an object.
"""

# SubTopic: Object Creation
"""
When a class is created then the design or blueprint
is only ready then we need to initialize or create a object
using constructors in python
then we can access the methods created inside the
class or mutate the object's attributes created using the init method.
"""

# SubTopic: Object Introspection
"""
Object introspection means to recognize the object
along with all its details, such as id or location.
One of the most basic ways to introspect is the type function.
Types of introspects:
    Some of the other common Introspects.
    1. hasattr(): It checks if an object has an attribute.
    2. getattr(): It returns the contents of an attribute if there are some.
    3. repr(): It returns the string representation of an object.
    4. vars(): It checks all the instance variables of an object.
    5. issubclass(): This function checks that if a specific class is a derived class of another class.
    6. isinstance(): It checks if an object is an instance of a specific class.
    7. __doc__: This attribute gives some documentation about an object.
    8. __name__: This attribute holds the name of the object.
    9. callable(): This function checks if an object is a function.
    10. help(): It checks what other functions do.
"""

# Topic: Inheritance
"""
Inheritance means to define a class that inherits
all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
We name these classes as parent and child because has they are the same in python as in real world
as only child can inherit the parent but not viceversa.
"""

# SubTopic: Types of Inheritance
"""
Types of inheritance:
    1. Single-level inheritance (It means only child class(B) is inheriting from the parent class(A)).
    
    2. Multi level inheritance (It means child class(B) is inheriting from parent class(A)
                                then child class(C) would inherit the parent class(B)).

    3. Multiple inheritance (It means a child class(C) inheriting from two parent classes(A,B)).

In inheritance when we inherit a parent class(A) to a child class(B).
When we execute B class then it find whether it has the init or
any method if it has the method then will execute the class B method or
if it does not have the method it will find the method in the parent class and then execute the method.
If we have the same method in both parent and child class then if we want to execute both methods from
both classes then we use a built-in function called "super" to represent the super/parent class.

In multiple inheritance if we have the init or any other method in both parent classes(A,B) and
parent classes(A,B) inherited by a child class(C) then if we want execute than it will execute the method from
first parent class from the left side because of MRO(Method Resolution Order), this order follows from left to right.
"""

# Topic: Polymorphism
"""
Polymorphism means multiple forms.
It means objects can have multiple forms
as also real life we people change according to the situation.
There are four ways of implementing polymorphism:
    1. Duck typing
    2. Operator overloading
    3. Method overloading
    4. Method overriding
"""

# SubTopic: Duck Typing
"""
The name Duck Typing comes from the phrase “If it looks like a duck and quacks like a duck, it’s a duck”.
Where the type or the class of an object is less important than the method it defines.
Using Duck Typing, We don't care about the class or the type of object created by the class.
We just care about does the required method exists or not.
"""

# SubTopic: Operator Overloading
"""
Operator overloading means giving extended meaning beyond their predefined operational meaning.
For example operator + is used to add two integers as well as join two strings and merge two lists.
It is achievable because ‘+’ operator is overloaded by int class and str class.
You might have noticed that the same built-in operator or function shows different behavior for objects
of different classes.
This is possible because python is object oriented so when we use operators
these operators will call a class like for example '+' it calls __add__ method.
So we add extra functionality to the method(__add__).
This is called Operator overloading.
"""

# SubTopic: Method Overloading and Overriding
"""
In python there is no method overloading because does not support it.
The concept of method overloading is that we create two methods with the same name but
both methods will have different number of parameters.
Of course these methods will be in the same class.
These is not supported because in python we can't create two methods with the same name but
we have work-around or tricks to do method overloading.

Method overriding means that when we have a child class(B) inherits parent class(A).
If child class(B) does not have a required method and the parent class(A) which is inherited,
has the method automatically the method in parent class(A) will be executed but
the moment when we have the required method in child class(B) then it will execute the method inside a child class(B)
not the the method from parent class(A) which is inherited.
This means the method from parent class(A) is overridden by the method from the child class(B).
This is called method overriding.
"""

# Topic: Abstract Methods and Classes
"""
Abstract method is a method which only has declaration and doesn't have definition.
It means it does not have any statements or body.
A class is called an abstract class only if it has at least one abstract method.
when you inherit a abstract class(A) to a child class(B),
the child class(B) should define all the abstract method present in parent class.
If it is not done then child class also becomes abstract class automatically.
Abstraction is not directly built-in into python so we use a module named "abc".
abc stands for Abstract Base Class by which we can make a class or method abstract.
"""

# Topic: Encapsulation
"""
Encapsulation means the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
To prevent accidental change, an object’s variable can only be changed by an object’s method.
"""

# SubTopic: Access Modifiers
"""
Encapsulation is achieved by using access modifiers.
There are three forms of access modifiers:
    1. Public (The members(Variables and Methods) of a class that are declared public are easily accessible
               from any part of the program.
               All data members and member functions of a class are public by default).
               
    2. Protected (The members of a class that are declared protected are only accessible to a class derived from it.
                  Data members of a class are declared protected by adding a single underscore ‘_’ symbol
                  before the data member of that class).
                  
    3. Private (The members of a class that are declared private are accessible within the class only,
                private access modifier is the most secure access modifier.
                Data members of a class are declared private by adding a double underscore ‘__’
                symbol before the data member of that class).
"""

# Topic: Context Managers
"""
Context managers will manage the usage of a resource like open and closing file
regardless of a error in code logically and in runtime.
A example of this is with keyword.
We can also create our own context managers with the module named contextlib.
"""

# Topic: Meta Classes (Type Class)
"""
Has in python, everything is a object than that means
a Class is also an object, and just like any other object, it’s a instance of something called Metaclass.
A special class type creates these Class object.
The type class is default metaclass which is responsible for making classes.
For example in above example if we try to find out the type of Student class, it comes out to be a type.
Because Classes are also an object, they can be modified in same way.
We can add or subtract fields or methods in class in same way we did with other objects.
Metaclass create Classes and Classes creates objects.
Metaclass is responsible for generation of classes,
so we can write our own custom metaclasses to modify the way classes are
generated by performing extra actions or injecting code.
Usually we do not need custom metaclasses but sometime it’s necessary.
"""

