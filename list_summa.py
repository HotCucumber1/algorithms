from data import SORTED_LIST


def summa(data: list[int]) -> int: 
    if data == []:
        return 0
    return data[0] + summa(data[1:])



print(summa(SORTED_LIST))