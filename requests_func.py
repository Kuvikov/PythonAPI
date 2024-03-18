import requests

payload = {"page": 8}

#post_data = {"id": "1"}
resource = requests.get("https://reqres.in/api/check_type", params=payload)
# resource1 = requests.post("https://reqres.in/api/check_type", data=post_data)
print(resource.json()['page'])

# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# print(r.url)
# # 200  <----- int
# print(r.headers)
# print(r.headers['content-type'])
# #'application/json; charset=utf8'
# print(r.encoding)
# #'utf-8'
# print(r.text)
# #'{"type":"User"...'
# print(r.json())
# # {'private_gists': 419, 'total_private_repos': 77, ...}
#
# response = requests.post('https://httpbin.org/post', data={'name': 'Maxim'})
# print(response.status_code)

# # Вывести url запроса
# print(response.url)
#
# #Запросы также поставляются со встроенным объектом поиска кода состояния для удобства использования
# r.status_code == requests.codes.ok
# #True
# ## Коды ответа
# # 100-199 - Информационные
# # 200-299 - Успех
# # 300-399 - Перенаправление
# # 400-499 - Ошибка клиента
# # 500-599 - Ошибка сервера
#
# if response.status_code == 200:
#     print("Ошибки нет, все отработано корректно")
# else:
#     print("Что-то пошло не так")
#
# #Перевести в формат JSON
# response = response.json()
# print(response['form'])

# Заголовки - headers

headers = {"Shlypa":"Super"}
sait_url = requests.get("https://reqres.in/api/check_type", headers = headers)

print(sait_url.headers)
print(sait_url.text)

# Cooke

payload = {"Login": "Kuvick", "Password": "P@ss"}
response = requests.get('https://api.github.com/user', data = payload)

print(response.json())
print(response.status_code)