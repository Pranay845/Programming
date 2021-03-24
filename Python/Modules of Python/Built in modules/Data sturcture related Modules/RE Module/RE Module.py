# Topic: Regular Expressions
"""
Regular expressions are used to perform search-related tasks in Python.
In this tutorial,
our primary focus should be on understanding because
we are going to cover a concept that has a wide range of uses.

To work with regular expressions,
we have to import a built-in module in python called ‘re’.
The module defines several functions and constants to work with RegEx.
The “re” module is composed of five functions known as:

findall: It finds all search for matches and print resultant in the form of a list.

search: It works the same as a findall, but the resultant is a matched object, if any found.

split: The split function splits the string from every matched into two new strings.

sub: The sub-function works exactly like a replace function in notepad or MS Word,
it replaces the original word, with a word of our choice.

finditer: The finditer yields an iterator as a resultant with all the objects that match the one we sent it
finditer supports more attributes than any other function defined above.
It also provides more details related to the matched object.

Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters
(characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string
"""

import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
'''

# Topic: findall, search, split, sub, finditer
patt = re.compile(r'')
patt = re.compile(r'.adm')
patt = re.compile(r'^Tata')
patt = re.compile(r'iin$')
patt = re.compile(r'ai{2}')
patt = re.compile(r'(ai){3}')
patt = re.compile(r'ai{3}|Fax')

# Topic: Special Sequences
patt = re.compile(r'Fax\b')
patt = re.compile(r'27\b')
patt = re.compile(r'\d{5}-\d{4}')

matches = patt.finditer(mystr)
for match in matches:
    print(match)
