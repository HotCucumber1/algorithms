from data import SORTED_LIST


def length(data: list[int]) -> int:
    if data == []:
        return 0
    return 1 + length(data[1:])


print(length(SORTED_LIST))