def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    
    result = []
    for first in lst:
        if first:
            result.append(first)
    return result     



   
    # return [val for val in lst if val]
