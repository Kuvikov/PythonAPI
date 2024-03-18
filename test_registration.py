import pytest, requests

class TestRegistraton:
    # login = [
    #     ('kuvikov@mail.ru'),
    #     ('123@mail.ru'),
    #     ('kuvikovmail.ru'),
    #     (''),
    #     ('kuvikov@mailru')
    # ]
    # password = [
    #     (12345),
    #     ('1234fd212'),
    #     (''),
    #     ('^&2107GFGUs'),
    #     ('/.,&'),
    # ]
    # @pytest.mark.parametrize('login', login, 'password', password)
    def test_registration(self):
        url = "https://reqres.in/api/users"
        registration = {
            "email": "kuvikov@reqres.in",
            "password": "Gg9asdasd12"
            }
        response = requests.post(url, data=registration)
        assert response.status_code == 201, 'Не успешный запрос на регистрацию'
        #assert 'auth_sid' in response.cookies, 'Нет такого пользователя'
        assert 'Content-Type' in response.headers, 'CSRF нет'
        assert 'id' in response.json(), 'user id в теле'

        # Content_Type = response.headers.get('Content-Type')
        # id = response.json()['id']
        #
        # response1 = requests.get(
        #     ''
        # )