from typing import List

BINGO_SELECTION_SIZE = 25


def get_bingo_selections() -> List[List[List[str]]]:
    with open("selections.txt") as f:
        readings = [int(num) for num in f.read().split()]
        flat_bingo_selections = [
            readings[i : i + BINGO_SELECTION_SIZE]
            for i in range(0, len(readings), BINGO_SELECTION_SIZE)
        ]
        grouped_bingo_selections = []
        for bingo_selection in flat_bingo_selections:
            grouped_bingo_selections.append(
                [bingo_selection[i : i + 5] for i in range(0, len(bingo_selection), 5)]
            )
    return grouped_bingo_selections


def get_numbers() -> List[int]:
    with open("numbers.txt") as f:
        readings = [int(num) for num in f.read().split(",")]
    return readings


def fill_number(bingo_selection: List[List[int]], chosen_num: int) -> List[List[int]]:
    for i, row in enumerate(bingo_selection):
        for j, num in enumerate(row):
            if num == chosen_num:
                bingo_selection[i][j] = -1
    return bingo_selection


def is_bingo(bingo_selection: List[List[int]]) -> bool:
    # check rows
    for row in bingo_selection:
        if all(num == -1 for num in row):
            # bingo
            return True

    # check columns
    for i in range(5):
        col = []
        for j in range(5):
            col.append(bingo_selection[i])
        if all(num == -1 for num in col):
            return True

    return False


def calculate_final_answer(
    filled_bingo_selection: List[List[int]], winning_num: int
) -> int:
    return (
        sum(
            filter(
                lambda val: val != -1,
                [val for row in filled_bingo_selection for val in row],
            )
        )
        * winning_num
    )


if __name__ == "__main__":
    bingos = get_bingo_selections()
    numbers = get_numbers()

    winner = None
    winning_num = 0
    while winner == None:
        for num in numbers:
            for index, bingo_selection in enumerate(bingos):
                updated_bingo_selection = fill_number(bingo_selection, num)
                if is_bingo(updated_bingo_selection):
                    print("Bingo!")
                    winner = index
                    winning_num = num
                    break
            else:
                continue
            break

    print(calculate_final_answer(bingos[index], winning_num))
