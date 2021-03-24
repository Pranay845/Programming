# Topic: HTTP
"""
HTTP stands for the 'Hypertext Transfer Protocol,'.
It is a set of protocols that are designed to enable communication between clients and servers.
Between clients and servers, it works as a request-response protocol.
To request a response from the server, we can request data from the server,
or we can submit data to be processed to the server.
"""

# Topic: Requests
"""
The response data depends on our type of request.
The request module is not a built-in Python module; instead, we have to download it manually.
Requests Module is used to send all kinds of HTTP requests.
It is also one of the most downloaded modules in Python because
all the web related software and programs must have it in them.
"""

# Topic: URL
"""
URL: this is the URL of the website where we want to send the request.
Params: this is a dictionary or a list of tuples used to send a query string.
Args: It is optional. It can be any named arguments offered by the get method.
"""

# Topic: How to send Request
"""
It is used to send a put request to a variable.
It is usually used to update or completely change the resources of a specific URL.
put():

Delete is used to delete the specific resource, specified by URL.
delete():

The head method returns a header for a specific resource
head():

Post requests take with it the data to the server to update it with.
post():

The patch is used to send patch requests.
It is used to apply partial modifications to a resource.
It carries with it the instructions for the modification.
patch():
"""

import requests
r = requests.get("")
print(r.text)

# status is like result for question

print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)

# Documentation: https://requests.readthedocs.io/en/v0.8.2/

# Documentation of HTTP Status Code: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
