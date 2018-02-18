# find() method, it specified the starting location of the original string
string = "welcome to the world of python"
print(string.find('the'))
print(string.find('of'))

# replace('1','2') method, in the we basically replace the original string with some other string
print(string)
print(string.replace('python', 'python3'))  # python is replaced by python3
string2 = "my name is aditya"
print("original string>>", string2, "<<after replacing the  string ", string2.replace('aditya', 'bhaskar'))

# split
print(string.split('-'))
string3 = 'a,b,c,d,e,f'
print(string3.split(','))  # it basically creates list of chracter

# count() and count('',beg,end)
print(string.count('t'))
print(string2.count('i', 0, 15))  # in this we specified the beg and end point

# upper()  basically convert sting into upper case
print(string2.upper())
print(string.upper())

# max()  #show maximum value from the alphabet
# it does not show the maximum occuring character
print(max(string))
print(max(string2))
print(max(string3))

# min()
string4 = "kfgoijdfbdfivhfjj"
print(min(string4))

# isalpha() #return ture if alphabet only occurs
print(string.isalpha())
print(string4.isalpha())

# lowe()
string5 = "ADITYA"
print(string5.lower())
