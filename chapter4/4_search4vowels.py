# set default argument
def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


# positional assignment
print(search4letters('abcde'))

# keyword assignment
print(search4letters(letters='xyz', phrase='xi ha yo'))
