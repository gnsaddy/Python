# working of string in python
name1 = "Aditya Raj"  # 1st way
name2 = 'Bhaskar uday'  # 2nd way
print(name1)
print(name2)
# print('i can't do work')  it does not work
print('i can\'t do work')
print("i can't do work")
# next line \n
print("hi there \n python is awesome")
# concatenation of string
print(name1 + "  " + name2)
print(name1 + "address")
# slicing of string
print(name1[3] + " " + name2[3])
print(name1[-2] + " " + name1[-5])  # from left to right
# for getting middle character
print(name1[2:6])
print(name2[3:7])
print(name1[5:])  # from desired char to end
print(name2[:9])
# length of a string
address = "New ashok nagar new Delhi"
print(len(address))
#
A = "Data"
B = "Analysis"
C = "Pandas"
print("{0} {1} using {2}".format(A, B, C))
