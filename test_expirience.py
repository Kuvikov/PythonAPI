class TestExample:
    # В случае, если функция будет начинаться не на test_** то pytest не проверит эту функцию
    def test_check_math(self):
        a = 5
        b = 9
        expected_summ = 14
        assert a+b == expected_summ, f'Бро {expected_summ} не равно сумме {a} и {b}'

    def test_check_math2(self):
        a = 5
        b = 99
        expected_summ = 14
        assert a+b == expected_summ, f'Бро {expected_summ} не равно сумме {a} и {b}'