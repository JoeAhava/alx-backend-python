#!/usr/bin/env python3
'''
Annotation complex and mixed [list]
'''


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''
    sum of list values annotated
    '''
    return sum(mxd_list)
