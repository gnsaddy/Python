Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[1,2,3,4,5,6,7,8]
>>> list #showing of list items
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list[3] #accessing item from the list
4
>>> list[6]
7
>>> list[4]=10 #changing value from given list
>>> list #showing the list after changing the value
[1, 2, 3, 4, 10, 6, 7, 8]
>>> list + [12,13,14] #adding value to the list temporary
[1, 2, 3, 4, 10, 6, 7, 8, 12, 13, 14]
>>> list #temporary value is deleted from the list
[1, 2, 3, 4, 10, 6, 7, 8]
>>> list.append(12,13,14)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list.append(12,13,14)
TypeError: append() takes exactly one argument (3 given)
>>> list.append(12)
>>> list.append(13) #adding value permantely by using append() function
>>> list #showing of new list
[1, 2, 3, 4, 10, 6, 7, 8, 12, 13]
>>> list[:8]
[1, 2, 3, 4, 10, 6, 7, 8]
>>> list[2:]
[3, 4, 10, 6, 7, 8, 12, 13]
>>> 
