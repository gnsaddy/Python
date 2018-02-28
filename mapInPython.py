first_list = [2, 3, 4, 5]
print("square roots:-", list(map(lambda x: x**3, first_list)))


def sqaureit(n):
    return n**2


print(list(map(sqaureit, first_list)))

squr_list1 = [2, 3, 4, 5]
squr_list2 = [6, 7, 8, 9]
print(list(map(lambda x, y: x * y, squr_list1, squr_list2)))

list_names1 = ['aditya', 'bhaskar', 'alok']
list_names2 = ['raj', 'uday', 'tripathi']


def proper(x, y): return x[0].upper() + x[1:] + ' ' + y[0].upper() + y[1:]


print(list(map(proper, list_names1, list_names2)))
