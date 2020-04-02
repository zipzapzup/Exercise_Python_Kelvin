import requests

# Documentation: https://docs.python.org/3/library/urllib.request.html
# Requests Bin - Inspect HTTP Requests
# Reqres.in - Fake API data
# HTTPBin - Fake API

r = requests.get('https://google.com')
print(r.status_code)