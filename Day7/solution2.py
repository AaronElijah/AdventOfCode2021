from typing import List, Tuple


def get_display_results() -> List[Tuple[List[str], List[str]]]:
    with open("input.txt", "r") as f:
        res = []
        for line in f.read().splitlines():
            patterns, display = line.split(" | ")
            patterns, display = patterns.split(" "), display.split(" ")
            res.append((patterns, display))
        return res


if __name__ == "__main__":
    res = get_display_results()

    # rules:
    # digit 0: 6 segments long + shares semgents with 1's but not with 4's
    # digit 1: only one that is 2 segments long
    # digit 2: 5 segments long and not subset of digit 6's segments
    # digit 3: 5 segments long and shares the same segments as 1's
    # digit 4: only digit that is 4 segments long
    # digit 5: 5 segments long and subset of 6's segments
    # digit 6: 6 segments long and doesn't share segments with 1
    # digit 7: 3 segments long only
    # digit 8: 7 segments long only
    # digit 9: 6 segments long and shares the same segments as 4

    # I know this is hideous and inefficient -> obviously you can do this with far fewer inspections of the segment patterns
    # I'm interested in speed of coding and readabiliy here, not the least time complexity
    output_values: List[int] = []
    for segment_values, outputs in res:
        digit_to_segment = {
            0: None,
            1: set(tuple(filter(lambda segment: len(segment) == 2, segment_values))[0]),
            2: None,
            3: None,
            4: set(tuple(filter(lambda segment: len(segment) == 4, segment_values))[0]),
            5: None,
            6: None,
            7: set(tuple(filter(lambda segment: len(segment) == 3, segment_values))[0]),
            8: set(tuple(filter(lambda segment: len(segment) == 7, segment_values))[0]),
            9: None,
        }
        digit_to_segment[9] = set(
            tuple(
                filter(
                    lambda segment: len(segment) == 6
                    and digit_to_segment[4].issubset(set(segment))
                    and digit_to_segment[1].issubset(set(segment)),
                    segment_values,
                )
            )[0]
        )
        digit_to_segment[0] = set(
            tuple(
                filter(
                    lambda segment: len(segment) == 6
                    and not digit_to_segment[4].issubset(set(segment))
                    and digit_to_segment[1].issubset(set(segment)),
                    segment_values,
                )
            )[0]
        )
        digit_to_segment[6] = set(
            tuple(
                filter(
                    lambda segment: len(segment) == 6
                    and not digit_to_segment[1].issubset(set(segment))
                    and not digit_to_segment[4].issubset(set(segment)),
                    segment_values,
                )
            )[0]
        )
        digit_to_segment[5] = set(
            tuple(
                filter(
                    lambda segment: len(segment) == 5
                    and set(segment).issubset(digit_to_segment[6]),
                    segment_values,
                )
            )[0]
        )
        digit_to_segment[3] = set(
            tuple(
                filter(
                    lambda segment: len(segment) == 5
                    and digit_to_segment[1].issubset(set(segment)),
                    segment_values,
                )
            )[0]
        )
        digit_to_segment[2] = set(
            tuple(
                filter(
                    lambda segment: len(segment) == 5
                    and not set(segment).issubset(digit_to_segment[6])
                    and not digit_to_segment[1].issubset(set(segment)),
                    segment_values,
                )
            )[0]
        )
        output_number = ""
        for output in outputs:
            for n, s in digit_to_segment.items():
                if set(output) == s:
                    output_number += str(n)
                    break
        output_values.append(int(output_number))
    print(output_values)
    print(sum(output_values))
