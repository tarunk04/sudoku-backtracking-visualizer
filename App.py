from sudoku import *
import copy
import eel

current_sudoku_onboard = []
updated_sudoku = []
solved_sudoku = []
# python functions exposed to javascript
@eel.expose
def generate_new_sudoku(level):
    global current_sudoku_onboard
    global updated_sudoku
    global solved_sudoku
    # generating sudoku for required level
    current_sudoku_onboard = Sudoku().generate_sudoku(int(level))
    updated_sudoku = copy.deepcopy(current_sudoku_onboard)
    # drawing sudoku by calling javascript function from python
    eel.draw_sudoku(current_sudoku_onboard)
    solved_sudoku = Sudoku().solve(current_sudoku_onboard,visualize=False,draw=False)


@eel.expose
def solve_sudoku(mode):
    global current_sudoku_onboard
    eel.draw_sudoku(current_sudoku_onboard)
    # solving the sudoku (quick mode or visualize)
    Sudoku().solve(current_sudoku_onboard, int(mode))

@eel.expose
def validate_sudoku(index,val):
    global updated_sudoku
    global solved_sudoku

    row = int(index)//9
    col = int(index)%9
    value = 0
    updated_sudoku[row][col] = value
    if val != "":
        value = int(val)
        eel.validate(index,Sudoku().validate_cell(updated_sudoku,value,row,col))
    else:
        eel.validate(index, True)
    updated_sudoku[row][col] = value
    if updated_sudoku == solved_sudoku:
        eel.done()


if __name__ == "__main__":
    # initializing eel with the dir containing HTML resources
    eel.init("www")

    # starting eel server
    eel.start('index.html', size=(540, 660))
