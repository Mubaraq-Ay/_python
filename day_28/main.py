# application programming interface (api)

# an api is a way for one piece of software to communicate with another piece of software.

# web api - a server exposes a certain url that when you send a request,
# they give you back data as json.

# breakdown of what happens.

# a server exists somewhere (a computer, running 24/7, owned by some company e.g bank, weather, etc)
# then the server defines the url you are allowed to request things from e.g. https://api.weather.com/lagos
# you send a request to the url (requests.get())
# then the server processes the request and send back a response (data in json format or a status code confirming something happened)

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
# print(response.status_code)
# print(response.json())

users = response.json()
print(users[0])

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(response.json())

response = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
print(response.json())


# mini user lookup script.

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()

for user in users:
     print(f"{user['name']} - {user['email']}")

for user in users:
    if 'e' in user['name'].lower():
        print(user['name'])

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()
print(len(posts))
print(posts[0]['title'])


# everytime you call requests.get('url'), we are doing something very specific which is;
# sending a structured message to a server and getting a structured message back. HTTP is the agreed upon format used for those messages.(like a shared language both sides understand)

# the request side (what i am sending)
# every http request has these parts:

# 1. a method: (what you want to do). the main ones are:
#       GET - (give me the data)
#       POST - (create something new with the data)
#       PUT - (updating something that already exists)
#       PATCH - (updating something partially)
#       
#       DELETE - (removing something)

# 2. a url - what you're asking about(e.g. https://jsonplaceholder.typicode.com/users/1 — "user number 1")
# 3. headers - extra information/metadata about the request itself
# 4. body - the actual data sent from client to a server (optional, mainly for POST/PUT)


# then response side (what you get back)
'''
    1. a status code: a number telling you what happened (e.g. 200, 403, etc)
    2. header - metadata about the response
    3. body - the actual data, usually json.
'''

'''
GET      → read
POST     → create
PUT      → replace/update
PATCH    → partial update
DELETE   → delete
'''

