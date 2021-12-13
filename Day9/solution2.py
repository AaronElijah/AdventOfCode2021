from typing import List, Tuple


def get_map() -> List[List[int]]:
    with open("input.txt", "r") as f:
        res = []
        for line in f.read().splitlines():
            res.append([int(point) for point in list(line)])
        return res


def calculate_basin_size(
    point: Tuple[int, int],
    map_: List[List[int]],
    previous_visited: List[Tuple[int, int]] = None,
) -> int:
    height = len(map_)
    width = len(map_[0])

    y_pos = point[0]
    x_pos = point[1]
    if previous_visited is None:
        previous_visited = []
    # try going left
    if (
        x_pos != 0
        and map_[y_pos][x_pos - 1] != 9
        and (y_pos, x_pos - 1) not in previous_visited
    ):
        previous_visited.append(point)
        calculate_basin_size((y_pos, x_pos - 1), map_, previous_visited)
    # try going down
    if (
        y_pos != height - 1
        and map_[y_pos + 1][x_pos] != 9
        and (y_pos + 1, x_pos) not in previous_visited
    ):
        previous_visited.append(point)
        calculate_basin_size((y_pos + 1, x_pos), map_, previous_visited)
    # try going right
    if (
        x_pos != width - 1
        and map_[y_pos][x_pos + 1] != 9
        and (y_pos, x_pos + 1) not in previous_visited
    ):
        previous_visited.append(point)
        calculate_basin_size((y_pos, x_pos + 1), map_, previous_visited)
    # try going up
    if (
        y_pos != 0
        and map_[y_pos - 1][x_pos] != 9
        and (y_pos - 1, x_pos) not in previous_visited
    ):
        previous_visited.append(point)
        calculate_basin_size((y_pos - 1, x_pos), map_, previous_visited)

    # add final point
    previous_visited.append(point)

    # when recursion is over, return final size
    return len(set(previous_visited))


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

    low_points_indices: List[Tuple[int, int]] = []
    for j, row in enumerate(low_points_map):
        for i, point in enumerate(row):
            if point is not None:
                low_points_indices.append((j, i))

    basin_sizes = sorted(
        [calculate_basin_size(position, map_) for position in low_points_indices],
        reverse=True,
    )
    print(basin_sizes)
    a, b, c = basin_sizes[:3]
    print(a * b * c)
