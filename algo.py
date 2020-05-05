import copy


class sudoku:
    def __init__(self, sudoku):
        self.sudoku_matrix = copy.deepcopy(sudoku)
        self.sudoku_solved = copy.deepcopy(sudoku)
        print(id(self.sudoku_matrix[0][0]))
        print(id(self.sudoku_solved[0][0]))

    def validate_cell(self, val, i, j):
        # getting index for block ( 9 blocks of 3x3 size)
        block_i = i // 3
        block_j = j // 3

        # check block
        for b_i in range(block_i * 3, block_i * 3 + 3):
            for b_j in range(block_j * 3, block_j * 3 + 3):
                if self.sudoku_solved[b_i][b_j] == val:
                    return False
        # check row
        for col in range(0, 9):
            if self.sudoku_solved[i][col] == val:
                return False

        # check column
        for row in range(0, 9):
            if self.sudoku_solved[row][j] == val:
                return False

        return True

    def __solve_backtrack__(self, i, j):
        # Changing row if col index reaches end of the row
        if j > 8:
            j = 0
            i += 1
            # end condition
            if i > 8:
                return True

        # skipping cell if the cell has already a number
        if self.sudoku_solved[i][j] != 0:
            if self.__solve_backtrack__(i, (j + 1)):
                return True
        # solving for the cell if the cell is empty
        else:
            # iterating over the possible values for the cell
            for val in range(1, 10):
                # validate the number for the cell
                if self.validate_cell(val, i, j):
                    # if validated fill the cell with the number
                    self.sudoku_solved[i][j] = val
                    # moving to next cell
                    if self.__solve_backtrack__(i, (j + 1)):
                        return True
                    # it the current validated number fails reset the cell
                    self.sudoku_solved[i][j] = 0
        return False

    def solve(self):
        self.__solve_backtrack__(0, 0)
        return self.sudoku_solved


if __name__ == "__main__":
    sudoku1 = [
        [5, 0, 0, 6, 0, 1, 0, 0, 0],
        [0, 3, 0, 0, 7, 5, 0, 4, 9],
        [0, 0, 0, 9, 4, 8, 0, 0, 0],
        [1, 5, 7, 0, 0, 0, 0, 0, 0],
        [0, 9, 6, 0, 0, 0, 2, 0, 8],
        [2, 0, 0, 1, 6, 9, 0, 5, 0],
        [4, 1, 0, 3, 0, 7, 0, 6, 0],
        [0, 2, 0, 5, 1, 0, 3, 7, 0],
        [7, 0, 3, 4, 0, 0, 1, 8, 0]
    ]

    sudoku_slover = sudoku(sudoku1)
    sudoku1 = sudoku_slover.solve()
    print(sudoku1)
