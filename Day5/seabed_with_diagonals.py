from typing import List, Union

from pprint import pprint


# We want the edges list to be [ [ (x1, y1), (x2, y2) ], ... ]
def get_edges() -> List[List[int]]:
    with open("input.txt", "r") as f:
        edges = []
        for line in f.readlines():
            vals = []
            for point in line.strip("\n").split(" -> "):
                vals.append(tuple(int(val) for val in point.split(",")))
            edges.append(vals)
    return edges


def edge_alignment(edge: List[List[int]]) -> str:
    if edge[0][0] == edge[1][0]:
        # vertical line
        return "vertical"
    elif edge[0][1] == edge[1][1]:
        # horizontal line
        return "horizontal"
    else:
        return "diagonal"


def fill_points(edge: List[List[int]]) -> List[List[int]]:
    if edge_alignment(edge) == "vertical":
        points_on_edge = [
            (edge[0][0], y)
            for y in range(min(edge[0][1], edge[1][1]), max(edge[0][1], edge[1][1]) + 1)
        ]
    elif edge_alignment(edge) == "horizontal":
        points_on_edge = [
            (x, edge[0][1])
            for x in range(min(edge[0][0], edge[1][0]), max(edge[0][0], edge[1][0]) + 1)
        ]
    else:
        vector_diff = (edge[1][0] - edge[0][0], edge[1][1] - edge[0][1])
        if vector_diff[0] > 0 and vector_diff[1] > 0:
            # +ve gradient in both axis
            points_on_edge = [
                (edge[0][0] + i, edge[0][1] + i) for i in range(vector_diff[0] + 1)
            ]
        elif vector_diff[0] < 0 and vector_diff[1] < 0:
            # -ve gradient in both axis
            points_on_edge = [
                (edge[0][0] - i, edge[0][1] - i) for i in range(abs(vector_diff[0]) + 1)
            ]
        elif vector_diff[0] > 0 and vector_diff[1] < 0:
            # +ve gradient in x axis, -ve gradient in y axis
            points_on_edge = [
                (edge[0][0] + i, edge[0][1] - i) for i in range(abs(vector_diff[0]) + 1)
            ]
        elif vector_diff[0] < 0 and vector_diff[1] > 0:
            # -ve gradient in x axis, +ve gradient in y axis
            points_on_edge = [
                (edge[0][0] - i, edge[0][1] + i) for i in range(abs(vector_diff[0]) + 1)
            ]
    return points_on_edge


def count_overlaps(plane: List[List[str]]) -> int:
    count = 0
    for i in range(1000):
        for j in range(1000):
            if plane[i][j] >= 2:
                count += 1
    return count


def solution():
    plane = []
    for _ in range(1000):
        row = []
        for _ in range(1000):
            row.append(0)
        plane.append(row)

    edges = get_edges()

    for edge in edges:
        points_on_edge = fill_points(edge)
        for point in points_on_edge:
            plane[point[0]][point[1]] += 1
    print(count_overlaps(plane))


if __name__ == "__main__":
    solution()
