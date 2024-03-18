import json

str_as_json = '{"name": "Maxim, Kuvikov"}'
obj = json.loads(str_as_json)

key = "name"
if key in obj:
    print(obj[key])
else:
    print(f'Ключа {key} в JSON нет')

a = 'Maxim'
print(type(a))
if type(a) == str:
    print('Это строка')
else:
    print('Сам понимаешь')
