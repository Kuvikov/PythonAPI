import pytest, requests

class TestFirstAPI:
    number_str = [
        (0),
        (1),
        (10),
        (''),
        ('Maxim'),
        ('$'),

    ]
    @pytest.mark.parametrize('number_str', number_str)
    def test_hello_call(self, number_str):
        url = "https://reqres.in/api/check_type"
        data = {'page': number_str}

        response = requests.get(url, params=data)
        assert response.status_code == 200, f'Ответ пришел с кодом НЕ 200'

        dict_response = response.json()
        assert 'page' in dict_response, f'Не JSON формат'

        if number_str == 0:
            number_dict_response = 1
        elif type(number_str) == str:
            number_dict_response = 1
        else:
            number_dict_response = number_str

        number = dict_response['page']
        assert number == number_dict_response, f'Значения не совпадают'