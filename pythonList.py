# list with empty value
initial_list = []
print(initial_list)
# list with some value
data_analysis_language = ['R', 'Python', 'SAS', 'Scala']
print(data_analysis_language)
data_analysis_language.append('java')
print(data_analysis_language)
# printing through index number
print(data_analysis_language[0])
print(data_analysis_language[1], data_analysis_language[2], data_analysis_language[3])
print(data_analysis_language[1:3])
print(data_analysis_language[0:2])
print(data_analysis_language[-1])   # negative indexing
print(data_analysis_language[-2])
no_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'aditya', 'raj']
print(no_list.pop(0))
print(no_list)
print(no_list.pop())  # it pop out the last element from the list
# conversion of string into list
a_setence = "Hi there i am Aditya raj and i love to code.I am a full stack java developer"
new_list_sentence = a_setence.split()
new_list_sentence1 = a_setence.split('.')
print(new_list_sentence1)
# conversion of list to string
b_senetence = ['R', 'Python', 'SAS', 'Scala']
print("-".join(b_senetence))
print(''.join(b_senetence))
print('----'.join(b_senetence))
c_sentence = ['hi', 'there', 'how', 'are', 'you', '   ??   ']
print('   &   '.join(c_sentence))
# multiplaction of list
list_a = ["hi"]
print(list_a * 10)
print(list_a + list_a)
