"""
Pandas is an open source data analysis library written in python.
It leverages the power and speed of numpy to make
data analysis and preprocessing easy for data scientists.
It provides rich and highly robust data operations.

Two types of data structures:
    Series:
    Its a one dimensional array with indexes.
    It stores a single column or row of data in a Dataframe.
    A one dimensional array (labeled) capable of holding any type of data.

    Dataframe:
    Its a tabular spreadsheet like structure representing
    rows each of which contains one or multiple columns.
    A two dimensional data (labeled) structure with columns
    of potentially different types of data.
"""

import numpy as np
import pandas as pd

# dict1 = {
#     "name": ["pranay", "madhav"],
#     "age": [44, 67]
# }

# A dataframe of dict1

# df = pd.DataFrame(dict1)
# print(df)

# To write into a csv file

# df.to_csv("Pandas.csv")
# df.to_csv("Pandas Index_False.csv", index=False)

# To see some rows from start and end in csv

# df.head(1)
# df.tail(1)


# df.describe()  # this does some math on numbers of dataframe

# to read a csv file

# df2 = pd.read_csv("Pandas.csv")

# print(df2["age"][0])

# to change a particular value in csv

# df2["age"][0] = 3

# to change index(row name) of the csv

# df2.index = ["first", "second"]

# Topic: Series
a = pd.Series(np.random.rand(34))
type(a)

# Topic: DataFrames and it's Methods
b = pd.DataFrame(np.random.rand(334, 5), index=np.arange(334))
type(b)

c = b.head()  # lists first few rows
print(c)

print(b)

d = b.describe()  # does some math operations on dataframe
print(d)

e = b.dtypes  # lists the type of rows
print(e)

f = b.index  # index means row name like s.no
print(f)

g = b.columns  # lists the columns
print(g)

b.to_numpy()  # changes dataframe to numpy array
print(b)

i = b.sort_index(axis=1, ascending=False)  # sorts the index
print(i)

j = type(i[0])  # lists the type of row
print(j)

k = b  # this only makes a pointer to before

k[0][0] = 123

print(k)
print(b)

l = b.copy()  # this totally copies the dataframe

b.loc[0, 0] = 345  # confirms the array which should be changed
print(b)

b.drop([0], axis=1)  # removes specified row/column

# Topic: Ways to use loc Method
ab = b.loc[[1, 2], :]

bc = b.loc[:, :]

cd = b.loc[:, [2, 3]]

ef = b.loc[(b[0] < 0.3) & (b[3] > 0.1)]

m = b.iloc[0, 4]  # lists the specified rows,columns
print(m)

n = b.iloc[[0, 4], [1, 2]]
print(n)

b.drop([0], axis=1, inplace=True)

b.reset_index()  # sets the index to original

b.reset_index(drop=True)

b.loc[[0]].isnull()

b.loc[[0]] = None

b.loc[:, [0]] = 34

b.dropna()  # Removes missing values.

b.drop_duplicates(subset=[2], keep=False)  # removes the duplicate ones

o = b.shape  # lists the shape of dataframe
print(o)

b.info()  # gives information about dataframe

b[0].value_counts(dropna=False)  # counts the value

b.notnull()  # checks for no nulls

print(b)

# Topic: Playing with Excel
# p = pd.read_excel("data.xlsx", sheet_name="sheet1")

# p.iloc[0, 0] = 87

# p.to_excel("data.xlsx", sheet_name="sheet1")

# Topic: Math Methods of DataFrames
dict1 = {
    "A": [34, 65],
    "B": [44, 67],
    "C": [34, 76]

}

q = pd.DataFrame(dict1)
r = q.describe()
print(r)

s = q.mean()
print(s)

t = q.corr()
print(t)

u = q.count()
print(u)

v = q.max()
print(v)

w = q.min()
print(w)

x = q.median()
print(x)

y = q.std()
print(y)

# Documentation: https://pandas.pydata.org/docs/
