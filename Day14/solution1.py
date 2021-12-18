import collections
from typing import Dict, List


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

    steps = 10
    polymer = template

    for _ in range(steps):
        pairs = get_polymer_pairs(polymer)
        new_polymer = ""
        for pair in pairs:
            molecule = pairings_map[pair]
            new_subchain = pair[0] + molecule
            new_polymer += new_subchain
        polymer = new_polymer + polymer[-1]
    print(polymer)
    element_count = collections.Counter(polymer).most_common()
    print(max(e[1] for e in element_count) - min(e[1] for e in element_count))
