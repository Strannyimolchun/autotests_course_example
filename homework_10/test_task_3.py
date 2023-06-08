# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smoke, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


class TestDivision:
    """Тесты деления"""

    @pytest.mark.parametrize('result, args, exception',
                             ((1, (10, 2, 5), False),
                              (pytest.param(0.16666666666666666, (1, 2, 3), False, marks=pytest.mark.smoke)),
                              (pytest.param(25.447387258410878, (71.1, 1.1, 2.54), False, marks=pytest.mark.skip('ссылка на ошибку'))),
                              (0, (0, 1.1, 2.54), False),
                              (None, (1, 0, 1), True)))
    def test_integer_result(self, result, args, exception):
        """Проверка деления:
        * Деление с целочисленным результатом
        * Деление с дробным результатом
        * Деление дробных чисел
        * Деление нуля
        * Деление на ноль
        """
        if exception:
            with pytest.raises(ZeroDivisionError):
                all_division(*args)
        else:
            assert all_division(*args) == result
