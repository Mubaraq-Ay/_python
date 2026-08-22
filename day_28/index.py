import requests

base_url = 'https://jsonplaceholder.typicode.com/users/1'

# 1. get (fetch the user first)
response = requests.get(base_url)
print(f'GET: {response.status_code}')
print(response.json())

# 2. put (update the user)
updated_data = {
    'name': 'mubaraq updated',
    'email': 'newmail@example.com',
}
response = requests.put(base_url, json=updated_data)
print(f'PUT: {response.status_code}')
print(response.json())

# 3. delete (remove the user)
response = requests.delete(base_url)
print(f'DELETE: {response.status_code}')