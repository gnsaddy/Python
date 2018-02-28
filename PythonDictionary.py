dict0 = {1: 'a', 2: 'b'}
print(dict0)
dict1 = {}  # empty dictionary
print(dict1)
# accessing the dict with the key value
print(dict0[1])

dict2 = {'name': 'aditya raj', 'address': 'new delhi', 'age': 20}
print("name:-", dict2['name'], "age:-", dict2['age'], "address:-", dict2['address'])
# adding a new key value
dict2['profession'] = 'Student'
print(dict2)
# checking the present key in a dict
print('address' in dict2)  # in keyword return the boolean value
# getting the list of keys and value from a existng dict
print(list(dict2.keys()))  # list of keys
print(list(dict2.values()))  # list of values

# dictionary creation using the dict keyword
new_dict = dict(country='India', state=['Delhi', 'Bihar', 'Maharastra', 'Rajasthan'])
print(new_dict)
# deleting value from the dictionary
del new_dict['state']
print(new_dict)
# dict length
print(len(dict2))
