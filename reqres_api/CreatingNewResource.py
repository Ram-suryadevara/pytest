import jsonpath
import requests
import json


# API URL
url = "https://reqres.in/api/users"

# read input json file
file = open(r"D:\Documents\txt_folder\usercreate.json", 'r')
json_input = file.read()

# parsing the file into json using loads.
request_json = json.loads(json_input)
print(request_json)

# Make post request with json input body
response = requests.post(url, request_json)
print(response.content)

# Validating response code
assert response.status_code == 201

# fetch header from response
print(response.headers.get('Content-Length'))

# parse response to json format
response_json = json.loads(response.text)

# pick id using json path
id = jsonpath.jsonpath(response_json, 'id')
print(id)
print(id[0])
