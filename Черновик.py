# def spell(*args):
#     k = {}
#     for i in [i.lower() for i in args]:
#         if i[0] in k:
#             if len(k[i[0]]) < len(i):
#                 k[i[0]] = i
#         else:
#             k[i[0]] = i
#
#         k[i[0]] = k.setdefault(i[0], i)
#     print(k)

# def spell(*args):
#     args = sorted([i.lower() for i in args], key=len)
#     k = {}
#     for i in args:
#         k[i[0]] = len(i)
#     print(k)
#
# def spell(*args):
#     # args = sorted([i.lower() for i in args], key=len)
#     k = {i[0]: len(i) for i in sorted([i.lower() for i in args], key=len)}
#     # for i in sorted([i.lower() for i in args], key=len):
#     #     k[i[0]] = len(i)
#     print(k)
#
# def spell(*args):
#     result = {}
#     for i in args:
#         if result.get(i[0].lower(), 0) < len(i):
#             result[i[0].lower()] = len(i)
#     print(result)
#
#
# words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
# spell(*words)
# # spell()


# def choose_plural(amount, declensions):
#     # if amount == 1:
#     #     k = str(amount) + declensions[0]
#     # elif 1 < amount < 5:
#     #     k = str(amount) + declensions[1]
#     # else:
#     #     k = str(amount) + declensions[2]
#     # return k
#     return declensions
#
# print(choose_plural(21, ('пример', 'примера', 'примеров')))

import itertools


def get_biggest(numbers):
    if numbers:
        k = list(itertools.permutations(numbers))
        # print('k = ', k)

        kk = [list(map(str, i)) for i in list(k)]
        # print('kk = ', kk)
        kkk = [''.join(i) for i in list(kk)]
        kkkk = list(map(int, kkk))
        kkkkk = max(kkkk)
        print(kkkkk)

        # print('kk = ', kk)
        # kk = sorted(k, key=)

    else:
        return -1


print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))