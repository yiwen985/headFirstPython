vowels = ['a', 'e', 'i', 'o', 'u']
# word = "Milliways"
word = input("Provide a word to search vowels: ")
found = []

# for letter in word:
#     if letter in vowels:
#         print(letter)

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(found)
