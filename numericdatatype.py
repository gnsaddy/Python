# numbers are the immutable in nature that means the value assigned to it, it can not be changed.
# basically Integers,floating point,complex no are fall into the category of python numbers.  They are defined as int, float and complex class in Python.

a1 = 100
print(a1, "is a kind of ")
print(type(a1))  # check which type of data is

a2 = 10.100
print(a2, "is a kind of ")
print(type(a2))   # check which type of data is

a3 = 3 + 5j  # this is a complex no.
print(a3, " is a kind of ")
print(type(a3))  # check which type of data is

# instance() method is used to check an object belong to a particular class, it basically return true or false
print(a1, "is a integer? ", isinstance(a1, int))
print(a2, " is a float? ", isinstance(a2, float))
print(a2, " is integer? ", isinstance(a2, int))
print(a3, " is complex? ", isinstance(a3, complex))

#in python there is no concept of double and long datatype,it is because Integer can be of any length,limited to the memory available
#floating number is accurate upto 15 decimal places. 
