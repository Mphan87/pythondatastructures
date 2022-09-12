from typing import Counter


def multiple_letter_count(phrase):
    
    result = {}

    for letters in phrase:
        result[letters] = result.get(letters,0) + 1


    return result  




    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """