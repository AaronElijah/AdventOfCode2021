import collections
from typing import Dict, List
import copy
import math


template = "FPNFCVSNNFSFHHOCNBOB"
# template = "NNCB"


def get_polymer_pairings() -> Dict[str, str]:
    with open("input.txt", "r") as f:
        # with open("input_test.txt", "r") as f:
        pairings = {}
        for line in f.read().splitlines():
            polymer, result = line.split(" -> ")
            pairings[polymer] = result
    return pairings


def get_polymer_pairs(polymer: str) -> List[str]:
    pairs = []
    for index in range(len(polymer) - 1):
        pairs.append(polymer[index : index + 2])
    return pairs


if __name__ == "__main__":
    pairings_map = get_polymer_pairings()

    steps = 40
    polymer = template
    pairs = get_polymer_pairs(polymer)
    pair_count = collections.Counter(pairs)

    for _ in range(steps):
        new_pair_count = {}
        for pair, count in pair_count.items():
            element = pairings_map[pair]
            first_new_subchain = pair[0] + element
            second_new_subchain = element + pair[1]
            if new_pair_count.get(first_new_subchain) is None:
                new_pair_count[first_new_subchain] = count
            else:
                new_pair_count[first_new_subchain] += count
            if new_pair_count.get(second_new_subchain) is None:
                new_pair_count[second_new_subchain] = count
            else:
                new_pair_count[second_new_subchain] += count

        pair_count = copy.deepcopy(new_pair_count)

    element_count = {}
    for pair, count in pair_count.items():
        e_1, e_2 = pair
        if element_count.get(e_1) is None:
            element_count[e_1] = count
        else:
            element_count[e_1] += count
        if element_count.get(e_2) is None:
            element_count[e_2] = count
        else:
            element_count[e_2] += count

    element_multiset = collections.Counter(element_count).most_common()
    print(element_multiset)
    print(
        math.ceil(max(e[1] for e in element_multiset) / 2)
        - math.ceil(min(e[1] for e in element_multiset) / 2)
    )
