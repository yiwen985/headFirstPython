# parenthese == generator

# it looks like tuplecomp, but isn't.
# it is a generator
for i in (x*3 for x in [1, 2, 3, 4, 5]):
    print(i)

# listcomp
lis = [x*3 for x in [1, 2, 3, 4, 5]]
print(lis)


# generator 和 comprehension 的区别:
# generator 拿到一个处理一个.
# comprehension 要全部处理完之后, 其它代码才可以执行, 如果数据量过大, 会引起内存不足