#!/usr/bin/env python3
'''
Annotation Callable
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    callable annotation
    '''
    return lambda x: x * x
