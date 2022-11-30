import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"

# send get request
response = requests.get(url)
# stored in response variable
print(response)

# Parse response to Json formath
# fetch specific value in the response using jsonpath
json_response = json.loads(response.text)
# print(json_response)

# Fetch value using json path
pages = jsonpath.jsonpath(json_response, "total_pages")
print(pages[0])

# Validating using assert
assert pages[0] == 2
