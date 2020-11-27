def apply(func: object, value: object) -> object:
    return func(value)

# apply(print, 123)
# print(apply(type, 123))
# print(apply(len, 'Marvin'))
# print(apply(type, apply))


def outer():
    def inner():
        print('This is inner.')
    
    print('This is outer, invoking inner.')
    inner()
    
# outer()

def outer1():
    def inner():
        print('This is inner.')
    
    print('This is outer, invoking inner.')
    return inner

# i = outer1()
# i()

# Use * to accept an arbitrary list of arguments
def myfunc(*args):
    for arg in args:
        print(arg, end=' ')
    if args:
        print('Have args.')
    else:
        print('no args.')
    
# myfunc(10, 20, 30, 40, 50, 60, 70)
# myfunc()
# values = [10, 20, 30, 40, 50, 60, 70]
# myfunc(values)
# myfunc(*values) # list -> individual arguments

# *  expand to a list of values.
# ** expand to a dictionary of keys and values.
def myfunc1(**args):
    for k, v in args.items():
        print(k, v, sep='->', end=' ')

# myfunc1(a=19, b=20)
# myfunc1(1,2,3) # error

def myfunc2(*args, **args1):
    for arg in args:
        print(arg, end=' ')
    for k, v in args1.items():
        print(k, v, sep='->', end=' ')

# myfunc2(1,2,3)
# myfunc2(a=10, b=20)
# myfunc2(1,2,3, a=10)
# myfunc2(a=10, 1,2,3) # error