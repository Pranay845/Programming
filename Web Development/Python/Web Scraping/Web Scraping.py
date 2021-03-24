import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

r = requests.get(url)
htmlContent = r.content
print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)

# Topic: Commonly used Types of Objects

# SubTopic: Tag
print(title)
print(type(title))

# SubTopic: NavigableString
print(title.string)
print(type(title.string))

# SubTopic: BeautifulSoup
print(soup)
print(type(soup))

# SubTopic: Comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2)
print(type(soup2.p.string))

# To get the title of the HTML page
title = soup.title

# To get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)

print(anchors)

# To get first element in the HTML page
print(soup.find('p'))

# To get classes of any element in the HTML page
print(soup.find('p')['class'])

# Find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# To get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# To get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()

# To get all the links on the page:
for link in anchors:
    if link.get('href') != '#':
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
for elem in navbarSupportedContent.contents:
    print(elem)

for item in navbarSupportedContent.strings:
    print(item)

for item in navbarSupportedContent.stripped_strings:
    print(item)

print(navbarSupportedContent.parent)

for item in navbarSupportedContent.parents:
    print(item.name)

print(navbarSupportedContent.next_sibling.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('.modal-footer')
print(elem)

elem = soup.select('#loginModal')[0]
print(elem)

# Documentation of bs4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Documentation of html5lib: https://html5lib.readthedocs.io/en/latest/html5lib.html
