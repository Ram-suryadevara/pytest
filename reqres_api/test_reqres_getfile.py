
import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
#Response<200>

#response.content() # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
#response.json() # This method is convenient when the API returns JSON

#How to Use Query Parameters
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
#print(response.json())

#Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})

#How to Access REST Headers
print(response.headers["date"])
#>>>> 'Wed, 11 June 2020 19:32:24 GMT'


#How to Check for HTTP Errors With Python Requests
response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests

#requests to raise an exception
#raise_for_status() function
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.

#TooManyRedirects
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.TooManyRedirects as error:
    print(error)

#max redirects
response = requests.get('http://api.open-notify.org/astros.json', max_redirects=2)

#disable redirects
response = requests.get('http://api.open-notify.org/astros.json', allow_redirects=False)

# ConnectionError
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    # Code here will only run if the request is successful
except requests.ConnectionError as error:
    print(error)

# 200+ means the request has succeeded.
# 300+ means the request is redirected to another URL
# 400+ means an error that originates from the client has occurred
# 500+ means an error that originates from the server has occurred

 