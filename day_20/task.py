import requests

romeo_and_juliet = 'https://www.gutenberg.org/files/1513/1513-0.txt'

response = requests.get(romeo_and_juliet)

print(response.status_code)
print(response.text[:500])