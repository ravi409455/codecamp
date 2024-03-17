def solution(board: list[list[str]]) -> bool:
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
    validated according to the following rules:

    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
      without repetition.
    """

    # def check_elements(items):
    #     elements_checked = set()
    #     for element in items:
    #         if element == ".":
    #             continue
    #         if element in elements_checked:
    #             return False
    #         if int(element) < 1 and int(element) > 9:
    #             return False
    #         elements_checked.add(element)

    #     return True

    # for row in board:
    #     if not check_elements(row):
    #         return False

    # for index in range(0, 9):
    #     all_column_elements = [row[index] for row in board]
    #     if not check_elements(all_column_elements):
    #         return False

    # for i in range(0, 9, 3):
    #     for j in range(0, 9, 3):
    #         all_elements = []
    #         for row in board[i : i + 3]:
    #             for item in row[j : j + 3]:
    #                 all_elements.append(item)

    #         if not check_elements(all_elements):
    #             return False

    # return True

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    block = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            curr = board[i][j]
            if curr == ".":
                continue
            if (curr in rows[i]) or (curr in cols[j]) or (curr in block[i // 3][j // 3]):
                return False
            rows[i].add(curr)
            cols[j].add(curr)
            block[i // 3][j // 3].add(curr)

    return True
