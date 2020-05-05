from algo import *
import eel

@eel.expose
def generate_new_sudoku():
    sudoku_gen = Sudoku().generate_sudoku(3)
    eel.draw_sudoku(sudoku_gen)

if __name__ == "__main__":
    eel.init("www")

    sudoku_gen = Sudoku().generate_sudoku(3)
    eel.draw_sudoku(sudoku_gen)
    sudoku_slover = Sudoku()

    eel.start('index.html',size=(540,660))
    sudoku1 = sudoku_slover.solve(sudoku_gen)
    for i in range(9):
        print(sudoku1[i])