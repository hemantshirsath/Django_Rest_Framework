import requests
import json

data={
    'name':"ranjit",
    'roll':202,
    'city':'Jalgaon'
}
data=json.dumps(data)
r=requests.post('http://127.0.0.1:8000/viewstu/',data=data)
response=r.json()
print(response)