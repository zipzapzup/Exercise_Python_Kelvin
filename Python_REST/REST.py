import requests

# Documentation: https://docs.python.org/3/library/urllib.request.html
# Requests Bin - Inspect HTTP Requests
# Reqres.in - Fake API data
# HTTPBin - REST server

r = requests.get('https://reqres.in/api/users/2')
print(r.status_code)
print(r.text)
print(r.json()['data']['email'])