
from typing import Tuple
from math import ceil


def get_landing_zone() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    with open("Day17/input.txt", 'r') as f:
        for line in f.read().splitlines():
            zones = line.split("target area: ")[1].split(", ")
            zones = tuple(tuple(map(lambda x: int(x), zones[i].split(axis)[1].split(".."))) for i, axis in enumerate(("x=", "y=")))
    return zones

if __name__ == "__main__":
    zones = get_landing_zone()
    y_min = zones[1][0]
    print(y_min * (y_min + 1) // 2)
    print(ceil(0.5*zones[1][0]**2))