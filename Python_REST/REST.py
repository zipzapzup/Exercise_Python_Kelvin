import requests

# Documentation: https://docs.python.org/3/library/urllib.request.html
# Requests Bin - Inspect HTTP Requests
# Reqres.in - Fake API data
# HTTPBin - REST server
# https://requestinspector.com/ HTTP Inspector on a WebHook

r = requests.get('https://reqres.in/api/users/2')
print(r.status_code)
print(r.text)
print(r.json()['data']['email'])


# Above Standard Python implementation
#
# Python URL Parameter manipulation
# p = requests.get('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf?key1=value1&key2=value2')


payload = {'key1': 'justone', 'key2': 'two'}
p = requests.get('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf', params=payload)

# HTTP Result: GET /inspect/01e4wrsthzddtj0rxqtzmttpaf?key1=justone&key2=two HTTP/1.1


# Requests with Headers
headers = {'my-token':'9sadf9sakdafiads9nvj213j901mn' }
FakeAgent = {'User-Agent': 'Fake-Agent'}
h = requests.get('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf', headers=headers)

# GET /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# Accept-Encoding: gzip
# User-Agent: python-requests/2.22.0
# Accept: */*
# My-Token: 9sadf9sakdafiads9nvj213j901mn


