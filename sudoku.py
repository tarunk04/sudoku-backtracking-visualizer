import copy
import random
import eel
import time


class Sudoku:
    def __init__(self):
        self.sudoku_matrix = []
        self.sudoku_solved = []
        self.counter = 0
        self.new_sudoku = []

    def validate_cell(self, sudoku_solved, val, i, j):
        # getting index for block ( 9 blocks of 3x3 size)
        block_i = i // 3
        block_j = j // 3

        # check block
        for b_i in range(block_i * 3, block_i * 3 + 3):
            for b_j in range(block_j * 3, block_j * 3 + 3):
                if sudoku_solved[b_i][b_j] == val:
                    return False
        # check row
        for col in range(0, 9):
            if sudoku_solved[i][col] == val:
                return False

        # check column
        for row in range(0, 9):
            if sudoku_solved[row][j] == val:
                return False

        return True

    def __solve_backtrack__(self, i, j, visualize=False):
        # Changing row if col index reaches end of the row
        if j > 8:
            j = 0
            i += 1
            # end condition
            if i > 8:
                if visualize == False:
                    eel.draw_sudoku(self.sudoku_solved)
                return True

        # skipping cell if the cell has already a number
        if self.sudoku_solved[i][j] != 0:
            if self.__solve_backtrack__(i, (j + 1), visualize):
                return True
        # solving for the cell if the cell is empty
        else:
            # iterating over the possible values for the cell
            for val in range(1, 10):
                # validate the number for the cell
                if self.validate_cell(self.sudoku_solved, val, i, j):
                    # if validated fill the cell with the number
                    self.sudoku_solved[i][j] = val
                    # moving to next cell
                    if visualize:
                        time.sleep(0.2)
                        eel.update_sudoku(val, 9 * i + j)
                        time.sleep(0.2)
                    if self.__solve_backtrack__(i, (j + 1), visualize):
                        return True
                    # it the current validated number fails reset the cell
                    self.sudoku_solved[i][j] = 0
                    if visualize:
                        time.sleep(0.2)
                        eel.update_sudoku(0, 9 * i + j)
                        time.sleep(0.2)
        return False

    def __count_solutions__(self, i, j):
        # Changing row if col index reaches end of the row
        if j > 8:
            j = 0
            i += 1
            # end condition
            if i > 8:
                self.counter += 1
                return

        # skipping cell if the cell has already a number
        if self.sudoku_solved[i][j] != 0:
            self.__count_solutions__(i, (j + 1))

        # solving for the cell if the cell is empty
        else:
            # iterating over the possible values for the cell
            for val in range(1, 10):
                # validate the number for the cell
                if self.validate_cell(self.sudoku_solved, val, i, j):
                    # if validated fill the cell with the number
                    self.sudoku_solved[i][j] = val
                    # moving to next cell
                    self.__count_solutions__(i, (j + 1))
                    # if the current validated number fails reset the cell
                    self.sudoku_solved[i][j] = 0
                    if self.counter > 1:
                        return

    def solve(self, sudoku, visualize=False):
        self.sudoku_matrix = copy.deepcopy(sudoku)
        self.sudoku_solved = copy.deepcopy(sudoku)
        self.__solve_backtrack__(0, 0, visualize=visualize)
        return self.sudoku_solved

    def solution_count(self, sudoku):
        self.sudoku_matrix = copy.deepcopy(sudoku)
        self.sudoku_solved = copy.deepcopy(sudoku)
        self.__count_solutions__(0, 0)

    def __generator__(self, grid, i, j):
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if j > 8:
            j = 0
            i += 1
            # end condition
            if i > 8:
                return True

        # skipping cell if the cell has already a number
        if grid[i][j] != 0:
            if self.__generator__(grid, i, (j + 1)):
                return True
        # solving for the cell if the cell is empty
        else:
            # iterating over the possible values for the cell
            random.shuffle(number)
            for val in number:
                # validate the number for the cell
                if self.validate_cell(grid, val, i, j):
                    # if validated fill the cell with the number
                    grid[i][j] = val
                    # moving to next cell
                    if self.__generator__(grid, i, (j + 1)):
                        return True
                    # it the current validated number fails reset the cell
                    grid[i][j] = 0
        return False

    def generate_solved_sudoku(self):
        # initializing the sudoku matrix
        solved_sudoku = []
        for i in range(9):
            solved_sudoku.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

        # generating sudoku using backtracking
        self.__generator__(solved_sudoku, 0, 0)
        self.new_sudoku = solved_sudoku

    def generate_sudoku(self, level=2):
        # generate solved sudoku
        self.generate_solved_sudoku()
        if level == 1:
            remove_cell = random.randint(32, 38)
        if level == 2:
            remove_cell = random.randint(40, 46)
        if level == 3:
            remove_cell = random.randint(48, 52)
        if level == 4:
            remove_cell = random.randint(54, 56)
        if level == 5:
            remove_cell = random.randint(59, 61)

        sudoku_board = copy.deepcopy(self.new_sudoku)
        # print(remove_cell)

        #all possible cells index
        index = []
        for i in range(81):
            index.append(i)

        while remove_cell > 0:
            cell_id = random.sample(index,1)[0]
            row = cell_id//9
            col = cell_id%9

            index.remove(cell_id)
            print(remove_cell)
            # while True:
            #     row = random.randint(0, 8)
            #     col = random.randint(0, 8)
            #     if sudoku_board[row][col] != 0:
            #         break

            back_up_val = sudoku_board[row][col]
            sudoku_board[row][col] = 0

            self.solution_count(sudoku_board)
            if self.counter > 1:
                sudoku_board[row][col] = back_up_val
            else:
                remove_cell -= 1
            self.counter = 0
            # break
        self.__print_board__(sudoku_board)
        return sudoku_board

    def __print_board__(self, board):
        for i in range(9):
            print(board[i])
        print("\n")
