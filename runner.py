from sudoku_final import SudokuSolver

game = SudokuSolver(
    "000000907000420180000705026100904000050000040000507009920108000034059000507000000")

print(game.board())
print(game.solve())
print(game.board())