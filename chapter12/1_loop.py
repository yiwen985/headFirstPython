import csv
from os import sep
from pprint import pprint
from datetime import datetime


# with open('buzzers.csv') as data:
#     print(data.read())

# with open('buzzers.csv') as data:
#     for line in csv.reader(data):
#         print(line)
        
# with open('buzzers.csv') as data:
#     for line in csv.DictReader(data):
#         print(line)

# with open('buzzers.csv') as data:
#     ignore = data.readline() # ignore the headerinfo
#     flights = {}
#     for line in data:
#         k, v = line.split(',')
#         flights[k] = v
# 
# pprint(flights)

# following characters are considered whitespace in strings: space, \t, \n, and \r.
# with open('buzzers.csv') as data:
#     ignore = data.readline() # ignore the headerinfo
#     flights = {}
#     for line in data:
#         k, v = line.strip().split(',')
#         flights[k] = v
# 
# pprint(flights)

# str.title(): to titlecase
# 19:00 -> 7:00   :datetime.convert2ampm
with open('buzzers.csv') as data:
    ignore = data.readline() # ignore the headerinfo
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint(flights)
print()
pprint(flights2)
print()

wests = [k for k, v in flights2.items() if v == 'West End']
print(wests)
print()

# for dest in set(flights2.values()):
#     print(dest, '->', [v for k, v in flights2.items() if v == dest])
flights3 = { dest: [k for k, v in flights2.items() if v == dest] for dest in set(flights2.values()) }
pprint(flights3)

# comprehension: 新建一个 dict, 用 for 循环处理已存在的 dict, 将产生的数据放到新建的 dict
# 
# destinations = []
# for dest in flights.values():
#     destinations.append(dest.title())
#
# built-in comprehensive:
# 1. more_dests = []
# 2. more_dests = [for dest in flights.values()]
# 3. more_dests = [dest.title() for dest in flights.values()]
# 
# more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}
#
# filter:
# just_freeport2 = {convert2ampm(k): v.title() for k, v in flights.items() if v == 'FREEPORT'}


# use for loop if you like
# flights3 = {}
# for k, v in flights2.items():
#     if v in flights3:
#         flights3[v].append(k)
#     else:
#         flights3[v] = [k]