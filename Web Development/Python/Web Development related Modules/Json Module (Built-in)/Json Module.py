# Topic: JSON
"""
JSON stands for JavaScript Object Notation. JSON is a data-interchange format, derived from JavaScript.
It is mostly used for storing or transferring data.
So, if we want our program to interact with the internet,
we must be familiar with this module
, even only to send or receive data through the internet.
It is one of Python's most important modules because,
however small level of our program is if we want it to interact only a bit through the internet,
the Json module must be imported first.
A JSON is an unordered collection of key and value pairs similar to a python dictionary.
The following are some important points about JSON.

Keys are unique strings that cannot be null.
Values can be anything from a String, Number, Tuple, Boolean, list, or null.
A JSON is represented by a string which is enclosed within curly braces { }
with keys-value pairs which are separated by a colon ( : ),
and pairs separated by a comma(, ).
"""

# Topic: JSON in Python
"""
JSON is already built-in in Python, so no need for an installation command.
We can import it so we may start working on it.
JSON module in Python helps us in converting the data structures to JSON strings.
Use the import function to import the JSON module in your Python program.

If we convert a JSON string to a Python, the resultant will be a dictionary.
The conversion is also known as parsing, and that is the keyword we use professionally for the conversion.
We can either convert from JSON to Python or from Python to JSON by using json.loads() or json.dumps() methods.
"""

# Topic: Methods
"""
load(): This method is used to load data from a JSON file into a python dictionary.
Loads( ): This method is used to load data from a JSON variable into a python dictionary.
dump():This method is used to load data from the python dictionary to the JSON file.
dumps(): This method is used to load data from the python dictionary to the JSON variable.

Parsing converts the code from one form to another,
making it compatible with running on the other platform
by changing all the little syntax differences and making it perfect for running on the other platform.
The following table shows how Python objects are converted to JSON objects.
"""

import json

data = '{"var1":"madhav", "var2":100}'
print(data)

parsed = json.loads(data)
print(type(parsed))

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('non', 540),
    "isgood": False
}

jscomp = json.dumps(data2)
print(jscomp)
