def hello_fun(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


# print(hello_fun('Hi', name='Aditya')
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)


test_var_args('yasoob', 'python', 'argv', 'test')

print('-------------------------------------------------------')


def student_info(*args, **kwargs):
    print("argument without key ",args)
    print("arguments with key ",kwargs)


student_info('Math', 'Science', name='Aditya', age=20)

print('-------------------------------------------------------')
