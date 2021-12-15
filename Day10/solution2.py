from statistics import median


def get_lines():
    with open("input.txt", "r") as f:
        res = []
        for line in f.read().splitlines():
            res.append(list(line))

    return res


if __name__ == "__main__":
    results = get_lines()

    bracket_pairs = {
        "<": ">",
        "{": "}",
        "[": "]",
        "(": ")",
    }

    close_bracket_to_score = {
        ">": 4,
        "]": 2,
        "}": 3,
        ")": 1,
    }
    scores = []
    for line in results:
        stack_counter = [line[0]]
        for bracket in line[1:]:
            if len(stack_counter):
                if bracket_pairs.get(stack_counter[-1]) == bracket:
                    stack_counter.pop()
                    continue
            stack_counter.append(bracket)

        for b in stack_counter:
            if b in close_bracket_to_score.keys():
                break
        else:
            # only incomplete lines at this point
            print(stack_counter)
            completion = []
            for b in stack_counter[::-1]:
                completion.append(bracket_pairs[b])

            sub_score = 0
            for b in completion:
                sub_score *= 5
                sub_score += close_bracket_to_score[b]

            scores.append(sub_score)

    print(median(sorted(scores)))
