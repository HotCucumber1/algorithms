def binary_search(data: list[int], n: int):
    first = 0
    last = len(data) - 1
    while (first <= last):
        middle = (first + last) // 2
        found = data[middle]
        if found == n:
            return middle
        if found > n:
            last = middle - 1
        else:
            first = middle + 1
    return None


my_list = list(range(1, 101))
n = 34
print(f'{n} имеет индекс \'{binary_search(my_list, n)}\'')
