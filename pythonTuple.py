# tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable in nature.It can not be modified.

name = ('a', 'd', 'i', 't', 'y', 'a')
print("tuple is", name)
num = (1, 2, 3, 4, 5, 6)
print(num)
# converting tuple into list
num2 = list(num)
print("tuple as list", num2)
num2.append('10')
print(num2)

print(num + (7, 8, 9))
num1 = num + (8, 7, 4, 1, 2, 3)
print(num1)
print("length of tuple", len(num1))

# converting of list into tuple
l_list = ["aditya", "raj"]
print(l_list)
t_tuple = tuple(l_list)
print(t_tuple)
# converting tuple into list
