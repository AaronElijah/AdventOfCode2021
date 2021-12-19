# cython: language_level=3
# distutils: language=c++

def get_nodes():
    with open("input_test.txt", "r") as f:
    # with open("input.txt", "r") as f:
        nodes = []
        for line in f.read().splitlines():
            nodes.append([int(point) for point in list(line)])
    return nodes


cdef expand_nodes(nodes):
    multiply_factor = 5

    new_nodes = []
    for _ in range(multiply_factor*len(nodes)):
        row = []
        for _ in range(multiply_factor*len(nodes[0])):
            row.append(0)
        new_nodes.append(row)

    for j in range(len(new_nodes)):
        for i in range(len(new_nodes[0])):
            r_i, original_i = divmod(i,  len(nodes[0]))
            r_j, original_j = divmod(j,  len(nodes))

            new_node_value = nodes[original_j][original_i] + (r_i + r_j)
            if new_node_value > 9:
                new_node_value = new_node_value % 9
            new_nodes[j][i] = new_node_value

    return new_nodes

cdef get_next_nodes(
    (int, int) current_node, visited_nodes, nodes,
):
    cdef int max_x = len(nodes[0])-1
    cdef int max_y = len(nodes)-1
    cdef int x
    cdef int y

    x, y = current_node
    if x == 0 and y == 0:
        next_nodes = [(1, 0), (0, 1)]
    elif x == 0 and y == max_y:
        next_nodes = [(0, y-1), (1, y)]
    elif x == max_x and y == 0:
        next_nodes = [(x-1, 0), (x, 1)]
    elif x == 0:
        next_nodes = [(x, y + 1), (x, y - 1), (x+1, y)]
    elif y == 0:
        next_nodes = [(x + 1, y), (x - 1, y), (x, y + 1)]
    elif x == max_x:
        next_nodes = [(x, y - 1), (x - 1, y), (x, y + 1)]
    elif y == max_y:
        next_nodes = [(x, y - 1), (x - 1, y), (x + 1, y)]
    else:
        next_nodes = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    unvisited_next_nodes = []
    for next_node in next_nodes:
        if next_node not in visited_nodes:
            unvisited_next_nodes.append(next_node)
    return unvisited_next_nodes


def solution():

    # IMPLEMENT DIJSTRA'S ALGORITHM
    nodes = get_nodes()
    nodes = expand_nodes(nodes)

    tentative_weights = []
    for row in nodes:
        row_weights = []
        for _ in row:
            row_weights.append(1e10)
        tentative_weights.append(row_weights)
    tentative_weights[0][0] = 0

    cdef set visited_nodes = set()
    cdef set unvisited_nodes = set()
    for j in range(len(nodes)):
        for i in range(len(nodes[0])):
            unvisited_nodes.add((i, j))

    cdef (int, int) initial_node = (0, 0)
    cdef (int, int) current_node = initial_node
    cdef (int, int) final_node = (len(nodes[0])-1, len(nodes)-1)
    while True:
        unvisited_next_nodes = get_next_nodes(current_node, visited_nodes, nodes)
        next_node_dist_map = {}
        for next_node in unvisited_next_nodes:
            tentative_dist = (
                nodes[next_node[1]][next_node[0]]
                + tentative_weights[current_node[1]][current_node[0]]
            )
            if tentative_dist < tentative_weights[next_node[1]][next_node[0]]:
                tentative_weights[next_node[1]][next_node[0]] = tentative_dist
                next_node_dist_map[next_node] = tentative_dist
            else:
                next_node_dist_map[next_node] = tentative_weights[next_node[1]][
                    next_node[0]
                ]

        visited_nodes.add(current_node)
        unvisited_nodes.remove(current_node)

        # find next node with smallest tentative distance
        next_node = None
        smallest_dist = None
        for node in unvisited_nodes:
            tentative_dist = tentative_weights[node[1]][node[0]]
            if tentative_dist == -1:
                continue
            else:
                if next_node is None and smallest_dist is None:
                    next_node = node
                    smallest_dist = tentative_dist
                elif tentative_dist < smallest_dist:
                    next_node = node
                    smallest_dist = tentative_dist
        if next_node == final_node:
            break

        current_node = next_node

    print(tentative_weights[-1][-1])
