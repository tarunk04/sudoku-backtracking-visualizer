from sudoku import *
import eel

current_sudoku_onboard = []

# python functions exposed to javascript
@eel.expose
def generate_new_sudoku(level):
    global current_sudoku_onboard
    # generating sudoku for required level
    current_sudoku_onboard = Sudoku().generate_sudoku(int(level))
    # drawing sudoku by calling javascript function from python
    eel.draw_sudoku(current_sudoku_onboard)


@eel.expose
def solve_sudoku(mode):
    global current_sudoku_onboard
    # solving the sudoku (quick mode or visualize)
    Sudoku().solve(current_sudoku_onboard, int(mode))


if __name__ == "__main__":
    # initializing eel with the dir containing HTML resources
    eel.init("www")

    # starting eel server
    eel.start('index.html', size=(540, 660))
