from typing import List, Tuple


def get_display_results() -> List[Tuple[str, str]]:
    with open("input.txt", "r") as f:
        res = []
        for line in f.read().splitlines():
            patterns, display = line.split(" | ")
            patterns, display = patterns.split(" "), display.split(" ")
            res.append((patterns, display))
        return res


if __name__ == "__main__":
    digit_to_number_segments = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
    }

    numbers_to_look_for = {1, 4, 7, 8}
    lengths_to_look_for = {digit_to_number_segments[num] for num in numbers_to_look_for}
    res = get_display_results()
    count = 0
    for _, display in res:
        for single_digit_display in display:
            if len(single_digit_display) in lengths_to_look_for:
                count += 1
    print(count)
