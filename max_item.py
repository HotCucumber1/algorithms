from data import SORTED_LIST


def max_item(data: list[int]) -> int:
    if data == []:
        return 0
    if max_item(data[1:]) > data[0]:
        return max_item(data[1:])
    return data[0]


print(max_item(SORTED_LIST))   