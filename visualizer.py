from algo import *
import eel
current_sudoku_onboard = []
@eel.expose
def generate_new_sudoku():
    global current_sudoku_onboard
    current_sudoku_onboard = Sudoku().generate_sudoku(3)
    eel.draw_sudoku(current_sudoku_onboard)
@eel.expose
def solve_sudoku():
    global current_sudoku_onboard
    Sudoku().solve(current_sudoku_onboard,True)

if __name__ == "__main__":
    eel.init("www")

    eel.start('index.html',size=(540,660))
    # sudoku1 = sudoku_slover.solve(sudoku_gen)
    for i in range(9):
        print(sudoku1[i])