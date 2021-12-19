from typing import Dict, List, Set, Tuple
from pprint import pprint
import time


def get_nodes() -> List[List[int]]:
    # with open("input_test.txt", "r") as f:
    with open("input.txt", "r") as f:
        nodes = []
        for line in f.read().splitlines():
            nodes.append([int(point) for point in list(line)])
    return nodes


def expand_nodes(nodes: List[List[int]]) -> List[List[int]]:
    multiply_factor = 5

    new_nodes = []
    for _ in range(multiply_factor * len(nodes)):
        row = []
        for _ in range(multiply_factor * len(nodes[0])):
            row.append(0)
        new_nodes.append(row)

    for j in range(len(new_nodes)):
        for i in range(len(new_nodes[0])):
            r_i, original_i = divmod(i, len(nodes[0]))
            r_j, original_j = divmod(j, len(nodes))

            new_node_value = nodes[original_j][original_i] + (r_i + r_j)
            if new_node_value > 9:
                new_node_value = new_node_value % 9
            new_nodes[j][i] = new_node_value

    return new_nodes


def get_next_nodes(
    current_node: Tuple[int, int],
    visited_nodes: Set[Tuple[int, int]],
    nodes: List[List[int]],
) -> List[Tuple[int, int]]:
    max_x = len(nodes[0]) - 1
    max_y = len(nodes) - 1

    # print(current_node)
    x, y = current_node
    if x == 0 and y == 0:
        next_nodes = [(1, 0), (0, 1)]
    elif x == 0 and y == max_y:
        next_nodes = [(0, y - 1), (1, y)]
    elif x == max_x and y == 0:
        next_nodes = [(x - 1, 0), (x, 1)]
    elif x == 0:
        next_nodes = [(x, y + 1), (x, y - 1), (x + 1, y)]
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


if __name__ == "__main__":

    # IMPLEMENT DIJSTRA'S ALGORITHM
    nodes = get_nodes()
    nodes = expand_nodes(nodes)

    tentative_weights = []
    for j, row in enumerate(nodes):
        row_ = []
        for i, _ in enumerate(row):
            row_.append(1e10)
        tentative_weights.append(row_)
    tentative_weights[0][0] = 0

    visited_nodes: Set[Tuple[int, int]] = set()
    unvisited_nodes: Set[Tuple[int, int]] = set()
    for j in range(len(nodes)):
        for i in range(len(nodes[0])):
            unvisited_nodes.add((i, j))

    available_nodes: Set[Tuple[int, int]] = set()

    initial_node = (0, 0)
    current_node = initial_node
    final_node = (len(nodes[0]) - 1, len(nodes) - 1)
    while True:
        unvisited_next_nodes = get_next_nodes(current_node, visited_nodes, nodes)
        next_node_dist_map: Dict[Tuple[int, int], int] = {}
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
        available_nodes = set.union(available_nodes, unvisited_next_nodes)

        start_time = time.time()

        # find next node with smallest tentative distance
        next_node = None
        smallest_dist = None
        for node in available_nodes:
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

        available_nodes.remove(next_node)
        current_node = next_node
        print(time.time() - start_time)

    pprint(tentative_weights[-1][-1])
