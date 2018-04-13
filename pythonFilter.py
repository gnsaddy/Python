from functools import reduce


def divide_by_3(x): return x % 3 == 0


my_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
div = filter(divide_by_3, my_list)
print(list(div))


q = reduce(lambda x, y: x + y, range(1, 5))
print(q)
