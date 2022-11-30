import jsonpath
import requests
import json
#API URL
url= "https://reqres.in/api/users/2"

# read input json file
file=open("D:\Documents\Createuser.json",'r')
json_input=file.read()
request_json=json.loads(json_input)
# print(request_json)

# Make post request with json input body
response=requests.put(url,request_json)
# print(response.content)

# Validating response code
assert response.status_code==200

# fetch header from response
# print(response.headers.get('Content-Length'))

# parse response to json format
response_json=json.loads(response.text)
updated_li=jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])

# pick id using json path
id=jsonpath.jsonpath(response_json,'id')
# print(id[0])
