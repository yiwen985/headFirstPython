
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}

# 注释下面的几条不会报错
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0

for letter in word:
    if letter in vowels:
        if letter in found:
            found[letter] += 1
        else:
            found[letter] = 1

for k, v in sorted(found.items()):
    print(k,'was found', v, 'time(s).')
