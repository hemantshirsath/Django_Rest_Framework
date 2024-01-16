import requests
import json

data={
    'id':2
}
data=json.dumps(data)
r=requests.delete('http://127.0.0.1:8000/viewstu/',data=data)
data=r.json()
print(data)