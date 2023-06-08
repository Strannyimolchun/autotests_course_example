# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestDivision:
    """Тесты деления"""

    @pytest.mark.smoke
    def test_integer_result(self):
        """Деление с целочисленным результатом"""
        assert all_division(10, 2, 5) == 1

    @pytest.mark.smoke
    def test_float_result(self):
        """Деление с дробным результатом"""
        assert all_division(1, 2, 3) == 0.16666666666666666

    def test_3(self):
        """Деление дробных чисел"""
        assert all_division(71.1, 1.1, 2.54) == 25.447387258410878

    def test_4(self):
        """Деление нуля"""
        assert all_division(0, 1.1, 2.54) == 0

    def test_5(self):
        """Деление на ноль"""
        with pytest.raises(ZeroDivisionError):
            all_division(1, 0, 1)
