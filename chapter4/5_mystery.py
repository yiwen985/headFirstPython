# by value  or  by reference
# mutable value   -> by reference
# immutable value -> by value
# immutable value: Strings, integers, and tuples


def double(arg):
    print('Before:', arg)
    arg = arg * 2
    print('After:', arg)

arg = 3
print(double(arg))

arg = [1,2,3]
print(double(arg))         # [1,2,3]  why?






# look at 'arg = arg * 2',
# assign a new reference to arg,
# the old reference still exists.