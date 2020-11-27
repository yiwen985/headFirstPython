def search4vowels(word):
    """Display any vowels found in an asked-word."""
    vowels = set('aeiou')
    # word = input('Provide a word to search for vowels: ')
    found = set(word).intersection(vowels)
    for vowel in found:
        print(vowel)
    return bool(found)


word = input('Provide a word to search for vowels: ')
search4vowels(word)

