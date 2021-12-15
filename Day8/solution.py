from typing import List, Set, Tuple


def get_display() -> List[Tuple[List[Set[str]], List[Set[str]]]]:
    with open("input.txt", "r") as f:
        res = []
        for line in f.read().splitlines():
            connections, displays = line.split(" | ")
            connections = connections.split(" ")
            displays = displays.split(" ")

            connections = [set(c) for c in connections]
            displays = [set(d) for d in displays]
            res.append((connections, displays))
    return res


if __name__ == "__main__":
    results = get_display()
    outputs = []

    for res in results:
        connections, displays = res
        number_to_connection = {
            0: None,
            1: next(filter(lambda c: len(c) == 2, connections)),
            2: None,
            3: None,
            4: next(filter(lambda c: len(c) == 4, connections)),
            5: None,
            6: None,
            7: next(filter(lambda c: len(c) == 3, connections)),
            8: next(filter(lambda c: len(c) == 7, connections)),
            9: None,
        }
        number_to_connection[9] = next(
            filter(
                lambda c: len(c) == 6 and number_to_connection[4].issubset(c),
                connections,
            )
        )
        number_to_connection[0] = next(
            filter(
                lambda c: len(c) == 6
                and not number_to_connection[4].issubset(c)
                and number_to_connection[1].issubset(c),
                connections,
            )
        )
        number_to_connection[6] = next(
            filter(
                lambda c: len(c) == 6
                and not number_to_connection[4].issubset(c)
                and not number_to_connection[1].issubset(c),
                connections,
            )
        )
        number_to_connection[5] = next(
            filter(
                lambda c: len(c) == 5 and c.issubset(number_to_connection[6]),
                connections,
            )
        )
        number_to_connection[3] = next(
            filter(
                lambda c: len(c) == 5
                and number_to_connection[1].issubset(c)
                and not c.issubset(number_to_connection[6]),
                connections,
            )
        )
        number_to_connection[2] = next(
            filter(
                lambda c: len(c) == 5
                and not number_to_connection[1].issubset(c)
                and not c.issubset(number_to_connection[6]),
                connections,
            )
        )

        output = ""
        for d in displays:
            for num, con in number_to_connection.items():
                if con == d:
                    output += str(num)
        outputs.append(int(output))
    print(sum(outputs))
