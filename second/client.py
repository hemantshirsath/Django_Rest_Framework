import requests 
import json

data={
    'name':'Hemant Shirsath',
    'age':21,
    'city':'Jalgaon'
}
json_data=json.dumps(data)
response=requests.post('http://127.0.0.1:8000/createstu/',data=json_data)
new_data=response.json()
print(new_data)