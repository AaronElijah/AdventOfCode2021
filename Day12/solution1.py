from os import path
from typing import Dict, List
from pprint import pprint


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
            next_node not in path or next_node.isupper()
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
