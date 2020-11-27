def search4vowels():
    """Display any vowels found in an asked-word."""
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels: ')
    found = set(word).intersection(vowels)
    for vowel in found:
        print(vowel)


search4vowels()

