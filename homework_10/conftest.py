# ----------------------------------------------------------------------------------------------------------------------
# X-UNIT-STYLE
# # для тестов в функциях
#
#
# # выполняется один раз до всех тестов в модуле
# def setup_module(module):
#     pass
#
#
# # выполняется один раз до каждой функции
# def setup_function(function=None):
#     pass
#
#
# # выполняется один раз после каждой функции, не вызывается если setup_function не выполнился
# def teardown_function(function=None):
#     pass
#
#
# # выполняется один раз после всех тестов в модуле, не вызывается если setup_module не выполнился
# def teardown_module(module):
#     pass
#
# # ----------------------------------------------------------------------------------------------------------------------
import time

# для тестов в классах
#
#
# class Test:
#
#     @classmethod
#     def setup_class(cls):
#         pass
#
#     def setup_method(self, method=None):
#         pass
#
#     def teardown_method(self, method=None):
#         pass
#
#     @classmethod
#     def teardown_class(cls):
#         pass
#
#     def test_1(self):
#         pass
#
#     def test_2(self):
#         pass

import pytest
from datetime import datetime as dt


@pytest.fixture(scope='class')
def start_stop_time(request):
    """Фикстура для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания"""
    print(f'Время начала тестов {request.node.name}: {dt.now()}')
    yield None
    print(f'\nВремя окончания тестов {request.node.name}: {dt.now()}')


@pytest.fixture()
def time_count(request):
    """Фикстура для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста"""
    start = dt.now()
    print()
    yield None
    print(f' - Время выполнения теста {request.node.name}: {dt.now() - start}')




# class TestOne(start_stop_time):
#
#     def test_1(self, time_count):
#         """Ждет 5 секунд и производит сложение"""
#         time.sleep(5)
#         assert 2 + 3 == 5
#
#     def test_2(self, time_count):
#         """Ждет 2 секунды и производит сложение"""
#         time.sleep(2)
#         assert 1 + 1 == 2


