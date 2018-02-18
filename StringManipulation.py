# working with string
''' string is a sequence of unicode characters.We can use single quotes or double quotes to represent strings.
Multiline string can be denoted using triple qootes '''  # '''string'''

string1 = 'single quote string in python'
string2 = "double quote string in python"
print(string1 + " and " + string2)

# string length function
print(len(string1))
print(len(string2))
# concatenation of strings
firstName = "Aditya"
secondName = "Raj"
cityName = "New Delhi"
print(firstName + " " + secondName + " city " + cityName)
# repetation of string
print(firstName * 3)
print(secondName * 3)
# string indexing
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[1])
print(alphabet[15])
print(alphabet[10])
print(alphabet[0:23])  # [start:end] of the string which we want
print(alphabet[3:10])
print(alphabet[0] + alphabet[20])
# reverse indexing of string
print(alphabet[-0])  # reverse indexing always start from [-1] index
print(alphabet[-18])
# slicing of string
print(firstName[1:3])
print(firstName[0:])
