from typing import Dict
import copy


def get_initial_fish():
    initial_fish = []
    with open("input.txt", "r") as f:
        for fish in f.readline().split(","):
            initial_fish.append(int(fish))
    # initial_fish = [3,4,3,1,2]
    fish_counts = {
        -1: 0,
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for fish in initial_fish:
        fish_counts[fish] += 1
    return fish_counts


def simulate(fish_count: Dict[int, int], num_days: int) -> Dict[int, int]:
    day = 0
    while day < num_days:
        new_fish_count = {
            -1: 0,
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        for i in range(8, -1, -1):
            new_fish_count[i - 1] = fish_count[i]
            if i == 0:
                new_fish_count[8] = fish_count[0]
                new_fish_count[6] = new_fish_count[6] + fish_count[0]
                new_fish_count[-1] = 0
        fish_count = copy.deepcopy(new_fish_count)
        print(fish_count)
        print(sum(val for val in fish_count.values()))
        day += 1
    return fish_count


def solution():
    fish_count = get_initial_fish()
    print(fish_count)
    print(simulate(fish_count, 256))


if __name__ == "__main__":
    solution()
