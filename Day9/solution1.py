from typing import List, Tuple


def get_map() -> List[List[int]]:
    with open("input.txt", "r") as f:
        res = []
        for line in f.read().splitlines():
            res.append([int(point) for point in list(line)])
        return res


if __name__ == "__main__":
    map_ = get_map()

    height = len(map_)
    width = len(map_[0])

    # initialize low point map
    low_points_map = []
    for j in range(height):
        row = []
        for i in range(width):
            row.append(None)
        low_points_map.append(row)

    # loop through every point and find low points
    for j in range(height):
        for i in range(width):
            # handle all edge and corner cases
            if i == 0 and j == 0:  # top left corner
                if map_[j][i] < map_[j][i + 1] and map_[j][i] < map_[j + 1][i]:
                    low_points_map[j][i] = map_[j][i]
            elif i == width - 1 and j == height - 1:  # bottom right corner
                if map_[j][i] < map_[j][i - 1] and map_[j][i] < map_[j - 1][i]:
                    low_points_map[j][i] = map_[j][i]
            elif i == 0 and j == height - 1:  # bottom left corner
                if map_[j][i] < map_[j][i + 1] and map_[j][i] < map_[j - 1][i]:
                    low_points_map[j][i] = map_[j][i]
            elif i == width - 1 and j == 0:  # top right corner
                if map_[j][i] < map_[j][i - 1] and map_[j][i] < map_[j + 1][i]:
                    low_points_map[j][i] = map_[j][i]
            elif i == 0:  # left side (vertical)
                if (
                    map_[j][i] < map_[j + 1][i]
                    and map_[j][i] < map_[j - 1][i]
                    and map_[j][i] < map_[j][i + 1]
                ):
                    low_points_map[j][i] = map_[j][i]
            elif i == width - 1:  # right side (vertical)
                if (
                    map_[j][i] < map_[j + 1][i]
                    and map_[j][i] < map_[j - 1][i]
                    and map_[j][i] < map_[j][i - 1]
                ):
                    low_points_map[j][i] = map_[j][i]
            elif j == 0:  # top side (horizontal)
                if (
                    map_[j][i] < map_[j + 1][i]
                    and map_[j][i] < map_[j][i - 1]
                    and map_[j][i] < map_[j][i + 1]
                ):
                    low_points_map[j][i] = map_[j][i]
            elif j == height - 1:  # bottom side (horizontal)
                if (
                    map_[j][i] < map_[j - 1][i]
                    and map_[j][i] < map_[j][i - 1]
                    and map_[j][i] < map_[j][i + 1]
                ):
                    low_points_map[j][i] = map_[j][i]
            else:
                if (
                    map_[j][i] < map_[j - 1][i]
                    and map_[j][i] < map_[j + 1][i]
                    and map_[j][i] < map_[j][i - 1]
                    and map_[j][i] < map_[j][i + 1]
                ):
                    low_points_map[j][i] = map_[j][i]

    risk = 0
    for row in low_points_map:
        for point in row:
            if point is not None:
                risk += point + 1
    print(risk)
