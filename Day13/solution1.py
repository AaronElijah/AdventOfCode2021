from typing import List, Tuple

from matplotlib import pyplot

folds = [
    ("x", 655),
    ("y", 447),
    ("x", 327),
    ("y", 223),
    ("x", 163),
    ("y", 111),
    ("x", 81),
    ("y", 55),
    ("x", 40),
    ("y", 27),
    ("y", 13),
    ("y", 6),
]


def get_coords() -> List[Tuple[int, int]]:
    with open("input.txt", "r") as f:
        coords = []
        for line in f.read().splitlines():
            x, y = line.split(",")
            coords.append((int(x), int(y)))

    return coords


if __name__ == "__main__":
    coords = get_coords()
    max_x = max(coord[0] for coord in coords)
    max_y = max(coord[1] for coord in coords)

    for fold in folds:
        reflect_line = fold[1]
        if fold[0] == "x":

            def reflect_coord(coord: Tuple[int, int]) -> Tuple[int, int]:
                if coord[0] > reflect_line:
                    new_coord = (2 * reflect_line - coord[0], coord[1])
                    return new_coord
                return coord

        else:

            def reflect_coord(coord: Tuple[int, int]) -> Tuple[int, int]:
                if coord[1] > reflect_line:
                    new_coord = (coord[0], 2 * reflect_line - coord[1])
                    return new_coord
                return coord

        coords = list(map(reflect_coord, coords))
    xs = [coord[0] for coord in coords]
    ys = [coord[1] for coord in coords]
    pyplot.scatter(xs, ys)
    pyplot.show()
