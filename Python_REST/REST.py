import requests
from requests.auth import HTTPBasicAuth

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

# GET is to REQUEST resources
# GET /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# Accept-Encoding: gzip
# User-Agent: python-requests/2.22.0
# Accept: */*
# My-Token: 9sadf9sakdafiads9nvj213j901mn


post = requests.post('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf')
# CRUD life (Create )
# POST is to CREATE Resources
#POST /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# Content-Length: 0
# Accept-Encoding: gzip
# Accept: */*
# User-Agent: python-requests/2.22.0


delete = requests.delete('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf')
# DELETE is to DELETE Resources
# DELETE /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# User-Agent: python-requests/2.22.0
# Accept-Encoding: gzip
# Accept: */*


put = requests.put('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf')

# PUT MODIFY all resources
# PUT /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# Content-Length: 0
# Accept: */*
# User-Agent: python-requests/2.22.0
# Accept-Encoding: gzip


patch = requests.patch('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf')

# PATCH ususally modify part of the resources
# PATCH /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# User-Agent: python-requests/2.22.0
# Accept-Encoding: gzip
# Accept: */*


payload1 = {'name': 'Bob', 'job':'CloudEngineer'}
j = requests.post('https://reqres.in/api/users', json=payload1)
print(j.text, j)


# Send form data
payload2 = {'name': 'Bob2', 'location': 'NSW'}
j2 = requests.post('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf', data=payload2)

# POST /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# Content-Length: 22
# Accept: */*
# Accept-Encoding: gzip
# User-Agent: python-requests/2.22.0
# Content-Type: application/x-www-form-urlencoded
# Raw
# name=Bob2&location=NSW

j3 = requests.post('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf', json=payload2)

# POST /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# User-Agent: python-requests/2.22.0
# Accept-Encoding: gzip
# Content-Type: application/json
# Content-Length: 35
# Accept: */*
# Json
# Raw
# {
#     "name": "Bob2",
#     "location": "NSW"
# }

payload3 = {'name':'Cool', 'location':'Melbourne'}
binreq = requests.post('https://httpbin.org/post', data=payload3 )
print(binreq.text)


# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "location": "Melbourne",
#     "name": "Cool"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "28",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0",
#     "X-Amzn-Trace-Id": "Root=1-5e859053-ec59cba00d8bd818832cf8c8"
#   },
#   "json": null,
#   "origin": "101.180.72.241",
#   "url": "https://httpbin.org/post"
# }


# POST Requests for Images sending picture
# Open in Binary
# MIME type
files = {'file' : open('Python_REST\\turtle.gif', 'rb')}
image = requests.post('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf', files=files)

# POST /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# User-Agent: python-requests/2.22.0
# Content-Type: multipart/form-data; boundary=783f0871d4da5bef69703617979caa80
# Accept: */*
# Accept-Encoding: gzip
# Content-Length: 7766

files2 = {'file' : ('turtle.gif', open('Python_REST\\turtle.gif', 'rb'), 'image/gif' )}
image2 = requests.post('https://requestinspector.com/inspect/01e4wrsthzddtj0rxqtzmttpaf', files=files2)


# POST /inspect/01e4wrsthzddtj0rxqtzmttpaf HTTP/1.1
# requestinspector.com
# Content-Type: multipart/form-data; boundary=63874a61ea6f2b389356ac7a99b72978
# User-Agent: python-requests/2.22.0
# Accept: */*
# Accept-Encoding: gzip
# Content-Length: 7791
# Raw
# --63874a61ea6f2b389356ac7a99b72978
# Content-Disposition: form-data; name="file"; filename="turtle.gif"
# Content-Type: image/gif



eror_catch = requests.get('https://httpbin.org/status/500')

try:
    eror_catch.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e, 'Error in GET')


### Basic Authentication

Basic = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=HTTPBasicAuth('user','passwd'))
print(Basic)

# <Response [401]> for Unauthorised
# <Response [200]> for Successful Authentication