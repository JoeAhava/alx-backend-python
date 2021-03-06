#!/usr/bin/env python3
'''
Annotation complex and mixed [tuple]
'''


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    sum of list values annotated
    '''
    return (k, v ** 2)
