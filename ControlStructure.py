# if condition
age = 21
if (age > 18):
    print("You can vote")
# if else statement
age = 17
if (age > 18):
    print("You can vote")
else:
    print("You can not vote")

# if elif else statement
print("Result")
mark = int(input("Enter number:-"))
passing = 40
destinction = 90
fail = mark < 40
if(mark >= 90):
    print("destinction mark,Extremelly good")
elif(mark >= 75 and mark < 90):
    print("You are passed,First class")
elif(mark >= 40):
    print("You are passed,good")
else:
    print("You are failed,attempt next time")

# check the first letter is vowel or not
input_string = input("Enter string:-")
first = input_string[0]
if(first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u'):
    print("YES")
else:
    print("NO")
