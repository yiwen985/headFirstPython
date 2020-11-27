# Learn 《Head First Python》

## chapter1

[find modules in STL](https://docs.python.org/3/library/index.html)

[find modules from Python community](https://pypi.org/)

find help:

1. Python 文档或参考书
2. dir: 显示相关联的属性, 如 dir(random), 可以找到 randint
3. help: 查看具体解释, 如 help(random.randint)

two ways of import:

1. from module import method(s): 该函数会被包含到当前文件，可以直接执行，执行时不会重新链接回模块。

>```python
>import datetime from datetime
># directly use datetime(), rather than datetime.datetime()
>```

2. import module

## chapter2

build-in data structure: list, dict, set, tuple

list features: array, dynamic size, heterogeneous, mutable, ordered

list-related methods:

* len(list)
* list(str), copy
* append, extend, +, insert
* pop, remove

support negative index.

slice: list[start:stop:step]

## chapter3

dict: unorderd

>遍历: `for k, v in dict.items():`
>
>access dict in dict: `persion['Ford']['age']`
>
>method `setdefault(k, v)` : if no key `k`, init with value `v`
>
>顺序输出: `for k, v in sorted(dict.items()):`
>
> easy to read: `import pprint`

set: unordered

> methods: union(), difference(), intersection()

tuple: unmutable, ordered

> `('python')` is a str, `('python',)` is a tuple

The 80/20 data structure rule：It’s the usual story with technologies designed to be generally useful: about 80% of what you need to do is covered, while the other, highly specific, 20% requires you to do more work.

the 4 built-in data structures solve the 80%.

## chapter4

注释: """comment"""

```python
str = """
        This is a str.
      """
```

modules: create, generate, install

> 1. how python search modules?
>
> three paths: current working directory(first), interpreter’s site-packages locations, STL locations
>> interpreter’s site-packages locations: `pip install` here
> 
> 2. create
>
> three things: setup.py, README.txt, modules(py files)
> 
> ```python
> # setup.py
> from setuptools import setup
> 
> setup(
>     name='vsearch',
>     version='1.0',
>     description='The Head First Python Search Tools',
>     author='xxx',
>     author_email='xxx',
>     url='xxx',
>     py_modules=['vsearch'],
> )
>
> ```
>
> 3. generate
> `py setup.py dist`
>
> 4. install
> `pip install xxx.tar.gz`
>

annotation: func(arg **: str**) **-> None:**

The goal of annotations is not to make life easier for the interpreter; it’s to make life easier for the user of your function. Annotations are a documentation standard, not a type enforcement mechanism.

## chapter5

create webapp using flask.

\_\_name\_\_ is called 'dunder name', rather than 'magic name'

## chapter6

file: open, read, close

## chapter7

connect using mysql

## chapter8

define class

## chapter9

`with` statment(context manager): class 中定义 \_\_enter\_\_ 和 \_\_exit\_\_ 方法, 参考 chapter7/webapp/DBcm.py

## chapter10

decorator(装饰器)

和 `with` 类似, decorator 旨在功能上的增强, with 则更强调上下文的环境, 例如 with 可以将与 MySQL 的连接的断开连接封装起来, 而 decorator 可以检查用户是否登录, 从而控制页面的跳转

## chapter11

exception

`sys.exc_info()`: Return exception information (type, value, traceback).

`def __exit__(self, exc_type, exc_val, exc_tb)`: 若 `with` 语句下面的代码块发生错误, 则可以传递到 \_\_exit\_\_

## chapter11 3/4

`t = Thread(target=method, args=(glacial, plodding, leaden))`

`t.start()`

如果执行很慢怎么办? it depends.
例如, 用户执行查询操作, 后台做2件事, 一是记录用户查询数据和其他相关信息, 二是将处理好的数据返回给用户. 因为用户不会关心后台是如何运作, 只希望得到结果, 而且记录用户查询数据是一个 SQL 插入语句, 可以独立出来运行, 因此前一件事情可以使用多线程. 但是处理数据的方法(do_research)执行完后, 会立即释放所占有的资源, 即 request 会被释放掉, 所以用到了 flask.copy_current_request_context.

## chapter12

comprehension, generator, yield

**comprehension**

understand a pattern:

1. start with a new dict or list

2. use a for loop process an existing dict

3. generating data for the new dict

```python
flights2 = {}
for k, v in flights.items():
  flights2[convert2ampm(k)] = v.title()

# comprehension
flights2 = {convert2ampm(k):v.title() for k, v in flights.items()}

# can add a filter
flights2 = {convert2ampm(k):v.title() for k, v in flights.items() if k == 'xxx'}
```

**generator**

```python
# this is a listcomp
li = [x*3 for x in [1,2,3]]
# this is a generator, not tuplecomp, and tuplecomp doesn't exist
for i in (x*3 for x in [1,2,3])
```

comprehension 和 generator 的区别: comprehension 是一次处理, 返回一个结果; 而 generator 是一次处理一个, 每次处理返回一个结果.

**yield**

generator -> functional generator
> don't use `return`, because it just return the result
>
> use `yield`, return the result every time you need it

```python
def gen_num():
  for i in (x*3 for x in [1,2,3]):
    yield i

for i in gen_num():
  print(i)
```

## Other

sorted won't change the order:

```text
>>> li = [1,5,2,4,3]
>>> sorted(li)
[1,2,3,4,5]
>>> li
[1,5,2,4,3]
```

no `++`, but `+= 1`

boolean: True, False

In Python everything is an object.

ternary operator（三元）：和其它语言的（？：）效果相等，如 `x = 10 if y > 3 else 20`

## 感想

A great book.
