# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    """Выводим в консоль параметры маркера"""
    marker = request.node.get_closest_marker('id_check')
    print()
    print(*marker.args, sep=', ')
