from random import choice

from data import UNSORTED_LIST


def qsort(data: list[int]) -> list[int]:
    if (len(data) < 2):
        return data
    base = data[0]
    less = []
    more = []
    for i in data[1:]:
        if i < base:
            less.append(i)
        else:
            more.append(i)
    return qsort(less) + [base] + qsort(more)


print(qsort(UNSORTED_LIST))
