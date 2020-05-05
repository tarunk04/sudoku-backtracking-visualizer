from algo import *

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

    # sudoku_slover = Sudoku()
    # sudoku1 = sudoku_slover.solve(sudoku1)
    # print(sudoku1)
    sudoku_gen = Sudoku().generate_sudoku(5)

    sudoku_slover = Sudoku()
    sudoku1 = sudoku_slover.solve(sudoku_gen)
    for i in range(9):
        print(sudoku1[i])