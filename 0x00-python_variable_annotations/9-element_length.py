#!/usr/bin/env python3
'''
Annotation ducked
'''


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    annotated ls
    '''
    return [(i, len(i)) for i in lst]
