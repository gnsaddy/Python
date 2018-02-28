new_list = ['a', 'a', 'b', 'b', 'c', 'c', 'aditya', 'raj', 'delhi', 20]
print("list :-", new_list)
# list as a set
new_set = set(new_list)
print("set:-", new_set)  # no data retadancy
print(type(new_set))  # to check the the type of class
# intersection union amd difference operation in set

list1 = ['a', 'a', 'b', 'd', 'f', 'g', 'r', 's', 'z']
set1 = set(list1)
print(set1)
list2 = ['b', 'h', 'j', 'e', 'a', 'z', 's', 'm', 'f']
set2 = set(list2)
print(set2)

print(set1.intersection(set2))  # shows the common elements
print(set1.union(set2))  # combination with no duplicate
print(set1.difference(set2))  # remove common
print(set1.symmetric_difference(set2))  # show the symmetric difference
# we also use ^ operator as a symmetric_difference
print(set1 ^ set2)
