# Python pip - Python package manager.
# pip - Preferred Installer Program. We use pip to install Python packages.
# A package is a collection of Python modules and can contain other packages.
# We don't need to write every utility ourselves; we can install packages
# and import them into our applications.

# installing pip.

# we install using -: pip install pip

# check pip version -: pip --version

# installing packages using pip.

# open any website

import webbrowser # module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)


# uninstalling packages.

# we use := pip uninstall packagename e.g. pip unistall numpy

# list of packages.
# we use pip list to see the installed packages on my machine.

# show package 
# to show information about a package.
# we use := pip show packagename e.g. pip show psutil
# to get more details, we use := pip show psutil --verbose


# pip freeze.
# this shows the installed packages with their version and the output suitable to use it in a requirements.txt file

# usage := pip freeze
# to save the list in a file we use:= pip freeze > requirements.txt

# reading from the url.
# an api is a way for two applications to communicate with each other.

# requests module contains the following

'''
    get(): sends a request to a url and fetches whatever is there, returns a response object (a package containing everything about what came back.)
    status_code(): a number telling you if the request succeded or failed.
    headers: extra info about the response itself
    text:  the actual contenr, as a plain string
    json: same as text, but automatically converts it into a python dict/list if the response is json data.
'''


import requests


url = 'https://ayanleke.cv'

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)