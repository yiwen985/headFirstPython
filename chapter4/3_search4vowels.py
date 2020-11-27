# annotation improve doc, no other behavior
# expect: arg is a str, return type is set

def search4vowels(word:str) -> set:
    """Display any vowels found in an asked-word."""
    vowels = set('aeiou')
    # found = set(word).intersection(vowels)
    return vowels.intersection(set(word))

# word = input('Provide a word to search for vowels: ')
word = [1,2,3]
print(search4vowels(word)) # successfully run



# The goal of annotations is not to make life easier for the interpreter; 
# it’s to make life easier for the user of your function. 
# Annotations are a documentation standard, not a type enforcement mechanism.