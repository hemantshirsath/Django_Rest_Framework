import requests
import json
data={
    
}
headers={'content-Type':'application/json'}
json_data=json.dumps(data)
response=requests.get('http://127.0.0.1:8000/viewstu/',headers=headers,data=json_data)
data=response.json()
print(data)