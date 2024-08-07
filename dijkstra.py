MY_GRAPH = {
    'start': {
        'a': 6,
        'b': 2,
    },
    'a': {
        'end': 1,
    },
    'b': {
        'a': 3,
        'end': 5,
    },
    'end': {},
}

costs = {   # from start
    'a': 6,
    'b': 2,
    'end': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'end': None
}

processed = []


def find_lowest_cost_node(costs) -> str:
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if (cost < lowest_cost) and (node not in processed):
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_way(graph):
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]  # цена до текущего узла

        neighbours = graph[node]  # соседи этого узла
        for n in neighbours:
            new_cost = cost + neighbours[n]  # цена до соседа
            if new_cost < costs[n]:
                costs[n] = new_cost  # обновляем цену до соседа
                parents[n] = node   # обновляем родителя соседа
        processed.append(node)
        node = find_lowest_cost_node(costs)
