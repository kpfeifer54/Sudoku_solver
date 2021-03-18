class SudokuSolver:

    def __init__(self, board_string: str):
        board = []
        for i in range(len(board_string)):
            if i % 9 == 0:
                temp_row = board_string[i:i+9]
                row = []
                for box in temp_row:
                    row.append(int(box))
                board.append(row)
        self.__board = board

    def board(self):
        string_builder = ""
        for i in range(9):
            if i % 3 == 0:
                string_builder += "---------------------\n"
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    string_builder += "| "
                if j == 8:
                    string_builder += str(self.__board[i][j]) + "\n"
                else:
                    string_builder += str(self.__board[i][j]) + " "
        string_builder += "---------------------\n"
        return string_builder

    def constraints(self, row, col, num):
        # Row
        for i in range(9):
            if self.__board[row][i] == num:
                return False

        # Col
        for i in range(9):
            if self.__board[i][col] == num:
                return False

        # Mini Box
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.__board[row][col] == num:
                    return False

        # If it passes all constraints, that means that we can place the number
        return True

    def solve(self):
        # Find a way to pick a spot on board
        for row in range(9):
            for col in range(9):
                if self.__board[row][col] == 0:
                    for num in range(1, 10):
                        if self.constraints(row, col, num):

                            # number that we changed..
                            self.__board[row][col] = num

                            if self.solve():
                                return "You solved the puzzle. Please choose another puzzle from the CSV file."

                            # BACKTRACK
                            self.__board[row][col] = 0

                    return False
        return True