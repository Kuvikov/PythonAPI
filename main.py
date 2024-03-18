import requests
from json.decoder import JSONDecodeError

payload = {"page": "hello"}
resource = requests.get("https://reqres.in/api/unknovn", payload)

try:
    parsed_response = resource.json()
    print(parsed_response)
except JSONDecodeError:
    print('Формат ответа не JSON')

# print(type(resource.text))
# print(type(resource.json()))
# print(resource.json()['data'])
# print('Hello world')

url = "https://reqres.in/api/users"
url2 = "https://reqres.in/api/users"

registration = {
                "email": "kuvikov@reqres.in",
                "password": "Gg9asdasd12"
                }
response = requests.post(url, data=registration)
response1 = requests.get(
    url2,
    #headers= {'id':301}
)
print(response.json())
print(response1.headers.get('token'))