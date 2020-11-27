# 'a', append mode
todos = open('todos.txt', 'a')
print('Put out the trash.', file=todos)
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
todos.close()

with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='') # not include newline character from print, use newline character from file