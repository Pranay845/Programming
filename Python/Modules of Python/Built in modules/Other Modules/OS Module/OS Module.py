"""
OS stands for Operating System.
"""

import os

a = dir(os)
print(a)  # it gives us a list of all the functions the OS module is composed of.

# The function returns us the path of the directory we are currently in.
b = os.getcwd()
print(b)

# Here cwd is a short form for the current working directory.
# It is important to know about our directory because when we are trying to import a file in python,
# The compiler searches for it in our current directory.

# If we want to access some files or folder from some other directory, we can use it.
os.chdir("C://")

# If we want to output the names of all the directories at a certain location,
# We can use this function.
c = os.listdir("C://")
print(c)

# To create a new directory or folder. The name is sent as a parameter inside the parenthesis.
os.mkdir("")

# To make more than on directory simultaneously.
os.makedirs("This/that")

# We send the current name and new name of our directory as parameters
os.rename("harry.txt", "man.txt")

# It deletes an empty directory.
os.rmdir("")

# We can remove all directories within a directory by using this
os.removedirs("")

# It will return us the environment variable.
# The environment variable must be set, or the function will return null.
os.environ.get("")

# It joins one or more path components.
# We can join the paths by simply using a + sign, but the benefit of using
# this function is that we do not have to worry about extra slashes between the components.
# So less accuracy still provides us with the same result.
os.path.join("")

# It returns us a Boolean value i.e., either true or false.
# It is used to check whether a path exists or not.
# If it does, then the output will be true, otherwise false.
d = os.path.exists("C://Program Files2")
print(d)

# It returns true if the path is an existing regular file.
e = os.path.isfile("")
print(e)

# It returns true if the path is an existing directory.
f = os.path.isdir("")
print(f)
