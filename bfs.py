from collections import deque


MY_GRAPH = {
    'me': ['A', 'B', 'C'], # root
    'A': ['D', 'E'],
    'B': ['F'],
    'C': [],
    'D': ['me'],
    'E': [],
    'F': ['G'],
    'G': []
}


def is_found(item):
    return item == 'F'


def init_queue():
    queue = deque()
    queue += MY_GRAPH['me']
    return queue


def search(queue):
    searched = []
    while queue:
        node = queue.popleft()
        if node not in searched:
            if is_found(node):
                print(node, 'is found')
                return True
        
            queue += MY_GRAPH[node]
            searched.append(node) 
    return False





queue = init_queue()
if not search(queue):
    print('Not found')
