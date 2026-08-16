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
for url in url_lists:
    webbrowser.open_new_tab(url)


# uninstalling packages.

# we use := pip uninstall packagename e.g. pip unistall numpy

