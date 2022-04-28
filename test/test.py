import requests
from pprint import pprint

'''data = requests.get("http://127.0.0.1:8080/api/university/1")
pprint(data)'''

data = requests.get("http://127.0.0.1:8080/api/university_list/пермь").json()
pprint(data)