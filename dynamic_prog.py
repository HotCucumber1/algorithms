from pprint import pprint


MAX_WEIGTH = 6

items = [
    {
        'name': 'water',
        'weight': 3,
        'cost': 10,
    },
    {
        'name': 'book',
        'weight': 1,
        'cost': 3,
    },
    {
        'name': 'food',
        'weight': 2,
        'cost': 9, 
    },
    {
        'name': 'jacket',
        'weight': 2,
        'cost': 5,
    },
    {
        'name': 'camera',
        'weight': 1,
        'cost': 6,
    },
]
cell = [[0 for _ in range(MAX_WEIGTH)] for _ in range(len(items))]

'''
Создаем таблицу, в которую записываем максимальный результат
на каждом этапе (для каждого веса), а затем берем максимум для текущего веса

Время выполнения: O(max_weigth * len(items))
'''
for i in range(len(items)):
    item = items[i]
    for j in range(MAX_WEIGTH):
        current_weight = j + 1
        if item['weight'] > current_weight:
            if i == 0:
                cell[i][j] = 0
            else:
                cell[i][j] = cell[i - 1][j]
            continue
        if i == 0:
            cell[i][j] = item['cost']
        elif j == 0:
            cell[i][j] = max(item['cost'], cell[i - 1][j])
        else:
            if j - item['weight'] >= 0:
                free_weight = cell[i - 1][j - item['weight']]
            else:
                free_weight = 0 
            cell[i][j] = max(item['cost'] + free_weight, cell[i - 1][j])  # формула для каждой задачи разная, а не универсальна


pprint(cell)
