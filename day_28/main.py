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

# status codes.
# every response comes back with a 3-digit number.

# the 5 categories.
'''
    1xx → Informational
    2xx → Success
    3xx → Redirection
    4xx → Client error
    5xx → Server error 
'''

'''
    1xx - rare, might not deal with these directly
    2xx = success
        200 - ok (the request worked, here's your data)
        201 - specifically for POST. created (a new request has been successfully created)
            e.g. POST /users → 201 Created
        204 - no content. (common for delete.) works but nothing to send back

    3xx - redirection.
        301 - moved permanently. means the url has been moved somewhere else
        302 - temporary redirection

    4xx - client error
        400 - bad request. (your request was malformed somehow)
        401 - unauthorized. you need to authenticate (login/provide credentials) to be able to access
        403 - forbidden. you're authenticated but not allowed to do this specific thing (e.g. a user trying to access the admin dashboard)
        404 - not found - what you asked for doesnt exist
        422 - unprocessable content. - well formed request but contains semantic errors
        429 - too many requests. - rate-limiting

    5xx - server error 
        500 - internal server error, - something broke on their end 
        502 - bad gateway. - invalid response received from an upstream server. (An upstream server is simply another server that a server depends on to complete your request.)
        503 - service unavailable - server is temporarily down
'''

# headers.
# headers are metadata about the request or response. (extra information about the message, seperate from the actual data/content itself.)

# common headers
# request headers (info you send)


headers = {
    'Content-Type': 'application/json', # the data im sending is json
    'Authorization': 'Bearer abc123token' # here is my auth token
}

# requests.get(url, headers=headers)

'''
    Content-Type       → what format is the body?
    Content-Length     → how large is the body?
    Content-Encoding   → was the body compressed?
    Cache-Control      → caching instructions
    ETag               → version/representation identifier
    X-RateLimit-*      → rate-limit information
'''

# response headers (info you receive back)

# response = requests.get(url)
# print(response.headers)
# Content-Type: application/json  -> "what I'm sending back is JSON"
# Content-Length: 1234            -> "the response body is this many bytes"


# body
# body is the actual data/content of the request or response

import requests

# Sending a body (POST) — creating a new user:
new_user = {
    'name': 'john',
    'email': 'john@gmail.vom'
}

# response = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user) # json=new_user is telling the request to convert it to json and send it as the body of the request
# print(response.status_code)
# print(response.json())

# receiving a body (GET)

response = requests.get('https://jsonplaceholder.typicode.com/users/1')
data = response.json()
print(data['name'])

# GET - no body is sent. body is received
# POST/PUT - body sent. new/updated data body often received back too (confirmation of what was created/updated)


# tsk

import requests

user = {
    'name': 'mubby',
    'email': 'mubby@gmail.com'
}

response = requests.post('https://jsonplaceholder.typicode.com/users', json=user)
print(response.status_code)
print(response.json())


# query parameters
# a query parameter lets you give extra instructions to an api about what you want.

'''
    example:

    https://example.com/users?country=Nigeria

    the part after the ? is the query string.
    country - is the parameter name
    Nigeria - is the parameter value.


    multiple parameters.

    it is seperated with &

    example:
    /users?country=Nigeria&limit=10

    meaning: Give me Nigerian users, but limit the result to 10.

    also, Path identifies the resource;
    query parameters provide additional instructions for the request.
'''

'''
    REST basics.

resource: is a thing your api manages.

endpoint: this is a specific api url you can interact with. it represents a resource.
example:

/users        <- endpoint for the users resource (collection resource)
/users/1      <- endpoint for one specific user (individual resource)

also:

GET    /users      -> read all users
GET    /users/1    -> read one user
POST   /users      -> create a new user
PUT    /users/1    -> update user 1
DELETE /users/1    -> delete user 1

RESTful url conventions (few rules):

Use nouns, not verbs, in URLs: /users not /getUsers (the method GET already says "get," don't repeat it in the URL)
Plural nouns for collections: /users not /user
Nest related resources logically: /users/1/posts — "posts belonging to user 1"

Statelessness: the server does not rely on remembering the previous request from the client. each request should contain the information the server needs to handle it.
         the server treats each request as if it's the first time it's heard from me.
'''


'''
    Authentication. (basics)
 - authentication: proving your identity (who are you?)
 - authorization: (what are you allowed to do?) e.g. trying to access a page for only admins

 btw, you can be authenticated but not authorized to do something.
'''

'''
    API keys.
    this is a secret string that identifies your app or account when talking to an api. (like a permanent password specifically for programmatic access. unchangeable btw, not tied to a login session)
'''

# e.g.

# headers = {
#     'Authorization': 'Api-Key abc123xyz'
# }

# requests.get(url, headers=headers)

'''
    bearer tokens

    this is a temporary credential proving you're currently authenticated. issued after you login, and sent in the header on every subsequent request (stateless)

    e.g. 
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'}
    requests.get(url, headers=headers)

    the long string is usually a jwt (json web token). a piece of data proving who you are, often with an expiration time built in.

    API key & token 
    api key - long-lived, identifies an app
    bearer token - often short lived, identifies a logged in user session
'''


'''
    sessions vs tokens
    two different startegies for staying logged in across multiple requests

    - sessions (stateful): older approach. Server maintains user state, allowing users to remain logged in
    across multiple requests without re-entering credentials.

    - tokens (stateless): the server doesnt store anything about your session. the token itself contains everything needed
    to verify who you are, and you just send it every request
'''