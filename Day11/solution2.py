from typing import List, Tuple

from pprint import pprint


def get_octopuses() -> List[List[int]]:
    with open("input.txt", "r") as f:
        # with open("input_test.txt", "r") as f:
        octopuses = []
        for line in f.read().splitlines():
            octopuses.append([int(o) for o in list(line)])
    return octopuses


def increase_by_one(octopuses: List[List[int]]) -> List[List[int]]:
    for j in range(len(octopuses)):
        for i in range(len(octopuses[0])):
            octopuses[j][i] += 1
    return octopuses


def find_flashing(octopuses: List[List[int]]) -> List[Tuple[int, int]]:
    flashing = []
    for j in range(len(octopuses)):
        for i in range(len(octopuses[0])):
            if octopuses[j][i] > 9:
                flashing.append((j, i))
    return flashing


def increase_energy(
    octopuses: List[List[int]], flashed_octopuses: List[Tuple[int, int]]
) -> List[List[int]]:
    for indices in flashed_octopuses:
        j, i = indices
        adjacent_octopuses = []
        if j == 0 and i == 0:  # top left corner
            adjacent_octopuses = [(j + 1, i), (j, i + 1), (j + 1, i + 1)]
        elif j == 0 and i == len(octopuses[0]) - 1:  # top right corner
            adjacent_octopuses = [(j + 1, i), (j + 1, i - 1), (j, i - 1)]
        elif j == len(octopuses) - 1 and i == 0:  # bottom left corner
            adjacent_octopuses = [(j - 1, i), (j, i + 1), (j - 1, i + 1)]
        elif (
            j == len(octopuses) - 1 and i == len(octopuses[0]) - 1
        ):  # bottom right corner
            adjacent_octopuses = [(j - 1, i), (j, i - 1), (j - 1, i - 1)]
        elif j == 0:  # top side
            adjacent_octopuses = [
                (j, i - 1),
                (j, i + 1),
                (j + 1, i - 1),
                (j + 1, i),
                (j + 1, i + 1),
            ]
        elif j == len(octopuses) - 1:  # bottom side
            adjacent_octopuses = [
                (j, i - 1),
                (j, i + 1),
                (j - 1, i - 1),
                (j - 1, i),
                (j - 1, i + 1),
            ]
        elif i == 0:  # left side
            adjacent_octopuses = [
                (j - 1, i),
                (j + 1, i),
                (j - 1, i + 1),
                (j, i + 1),
                (j + 1, i + 1),
            ]
        elif i == len(octopuses[0]) - 1:  # right side
            adjacent_octopuses = [
                (j - 1, i),
                (j + 1, i),
                (j - 1, i - 1),
                (j, i - 1),
                (j + 1, i - 1),
            ]
        else:  # bulk
            adjacent_octopuses = [
                (j - 1, i),
                (j - 1, i + 1),
                (j, i + 1),
                (j + 1, i + 1),
                (j + 1, i),
                (j + 1, i - 1),
                (j, i - 1),
                (j - 1, i - 1),
            ]
        for indices in flashed_octopuses:
            y, x = indices
            octopuses[y][x] = -1
        for adj in adjacent_octopuses:
            y, x = adj
            if adj not in flashed_octopuses:
                if octopuses[y][x] != -1:
                    octopuses[y][x] += 1

    return octopuses


if __name__ == "__main__":
    octopuses = get_octopuses()

    num_steps = 1000
    cur_step = 0
    total_flases = 0

    all_flashed = 0
    while cur_step < num_steps:
        octopuses = increase_by_one(octopuses)
        while len(find_flashing(octopuses)) > 0:
            flashed_octopuses = find_flashing(octopuses)
            octopuses = increase_energy(octopuses, flashed_octopuses)
            total_flases += len(flashed_octopuses)

        cur_step += 1

        for j in range(len(octopuses)):
            for i in range(len(octopuses[0])):
                if octopuses[j][i] == -1:
                    octopuses[j][i] = 0

        all_flashed = sum([sum(e) for e in octopuses]) == 0
        if all_flashed:
            print(cur_step)
            break
