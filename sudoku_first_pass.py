class SudokuSolver:

  def __init__(self, board_string):
    self.board_string = list(board_string)

  def solve(self):
    #adding a while loop so that we can keep starting over every time a new number is added until the board is solved
    index = 0
    while index < len(self.board_string):
      # start in the top left corner cell and go through each cell
      #only need to solve for numbers that are 0
      if int(self.board_string[index]) != 0:
        index += 1
      else:
        # set possible numbers to 1-9
        possible_numbers = [1,2,3,4,5,6,7,8,9]

        # look at all numbers in the row, eliminate any numbers that appear
        row = self.get_row(index)
        for num in row:
          if num in possible_numbers:
            possible_numbers.remove(num)

        # look at all numbers in the column, eliminate any numbers that appear
        column = self.get_column(index)
        for num in column:
          if num in possible_numbers:
            possible_numbers.remove(num)

        # look at all numbers in the square, eliminate any numbers that appear
        square = self.get_square(index)
        for num in square:
          if num in possible_numbers:
            possible_numbers.remove(num)

        # if only 1 number is left, that number goes in the cell
        if len(possible_numbers) == 1:
          cell_solution = possible_numbers[0]
          #write the solution to the board
          self.board_string[index] = cell_solution
          index = 0
          solved_flag = True
        else:
          solved_flag = False
          index += 1
    if solved_flag == True:
      print('Solved!')
    print(self.board_string)
    return(self.board_string)

  def board(self):
    pass
    
  def get_row(self, index):
    #this will return an array with all numbers in a given row
    first_cell = index - (index % 9)
    row_list = []
    for i in range(first_cell, first_cell + 9):
      row_list.append(int(self.board_string[i]))
    return row_list
  
  def get_column(self, index):
    #this will return an array with all numbers in a given column
    column_list = []
    ref_list = [0,9,18,27,36,45,54,63,72]
    remainder = index % 9
    index_list = [x+remainder for x in ref_list]
    for i in index_list:
      column_list.append(int(self.board_string[i]))
    return column_list
  
  def get_square(self, index):
    square_list = []
    first_cell = index - (index % 3)
    if (index // 9) % 3 == 2:
      first_cell = first_cell - 18
    elif (index // 9) % 3 == 1:
      first_cell = first_cell - 9

    for i in range(first_cell, first_cell+3):
      square_list.append(int(self.board_string[i]))
    for i in range(first_cell+9, first_cell+12):
      square_list.append(int(self.board_string[i]))
    for i in range(first_cell+18, first_cell+21):
      square_list.append(int(self.board_string[i]))
    return square_list


# The file has newlines at the end of each line, so we call
# String#chomp to remove them.
# game = SudokuSolver(board_string)
# # Remember: this will just fill out what it can and not "guess"
# game.solve

# print(game.board)

# s = SudokuSolver('530070000600195000098000060800060003400803001700020006060000280000419005000080079')
# s.solve()

s2 = SudokuSolver('200080300060070084030500209000105408000000000402706000301007040720040060004010003')
s2.solve()