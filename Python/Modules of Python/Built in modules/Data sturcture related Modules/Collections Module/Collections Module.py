"""
Collections Module provides more functionality and
alternatives to basic container types like list,tuple,set,dict.
"""

from collections import deque, namedtuple, Counter

# Topic: Counter
"""
Counter is like dict but with more features.
"""

print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

# Subtopic: Counter with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))

# Subtopic: Counter with keyword argument
a = Counter(A=3, B=5, C=2)
print(a["B"])

# Topic: namedtuple
"""
namedtuple is like combination of fstrings and tuples.
"""

c = namedtuple("e", 'x y z')
d = c(3, 4, 5)
print(d)
e = deque("""pranay""", maxlen=3)
print(e)
e.extendleft("madhav")
print(e)
