from os import path
from typing import Dict, List
from pprint import pprint
from collections import Counter


def get_edges() -> Dict[str, List[str]]:
    # with open("input_test.txt", 'r') as f:
    # with open("input_test_2.txt", 'r') as f:
    # with open("input_test_3.txt", 'r') as f:
    with open("input.txt", "r") as f:
        edge_map = {}
        for line in f.read().splitlines():
            a, b = line.split("-")
            if edge_map.get(a):
                edge_map[a] = edge_map[a] + [b]
            else:
                edge_map[a] = [b]
            if edge_map.get(b):
                edge_map[b] = edge_map[b] + [a]
            else:
                edge_map[b] = [a]
    return edge_map

def is_able_visit_next_node(next_node: str, cur_path: List[str]) -> bool:
    if next_node == "start":  # cannot revisit start node
        return False

    if next_node.isupper():
        return True
    # check for if a single small cave has been visited twice
    node_count = Counter(cur_path)
    
    for key, value in node_count.items():
        if key.islower() and value == 2:
            if key == next_node:
                return False  # cannot visit a small cave three times
            else:
                if node_count[next_node] == 0:  # can visit a small cave at least once but cannot visit two small caves twice
                    return True
                else:
                    return False
    else:
        return True  # no small caves have been visited twice

def find_paths(
    edge_map: Dict[str, List[str]], path: List[str], all_paths: List[List[str]]
):
    cur_node = path[-1]

    if cur_node == "end":  # full path found
        all_paths.append(path)
        return

    cur_path_length = len(path)
    for next_node in edge_map[cur_node]:
        if (
            is_able_visit_next_node(next_node, path)
        ):  # check the current node hasn't been visited or is an upper case big cave
            path = path + [next_node]
            find_paths(edge_map, path, all_paths)
            # set path to always be at the cur_node at this point
            path = path[:cur_path_length]

    return all_paths


if __name__ == "__main__":
    edge_map = get_edges()
    print(edge_map)
    print("****")
    paths = find_paths(edge_map, ["start"], [])
    pprint(paths)
    print(len(paths))
