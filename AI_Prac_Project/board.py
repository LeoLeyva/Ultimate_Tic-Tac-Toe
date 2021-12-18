import exceptions as ex


class Board:

  #######Private#######
  
  __matrix = []
  __rows = 9
  __cols = 9
  alpha_to_num= {"A": 0, "B":1, "C": 2, "D":3, "E":4,"F":5,"G":6,"H":7,"I":8}
  moves_left = {"0":9, "1":9, "2":9,"3":9,"4":9,"5":9, "6":9,"7":9, "8":9}
  coords_to_board = {(0,0):"0", (1,0):"1", (2,0):"2",(0,1):"3",(1,1):"4",(2,1):"5",(0,2):"6",(1,2):"7",(2,2):"8"}

  board_winners =  {
      "0": "", "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": ""}

  def __init__(self):

    for l in range(0,9):
      mid_row = []
      for k in range(0, 9):
        mid_row.append(" ")
      self.__matrix.append(mid_row)

  def __valid_board_check(self, next_move, intended_move):
    n_mv_left = self.moves_left[next_move]
    i_mv_left = self.moves_left[intended_move]

    if next_move == intended_move:
      if n_mv_left == 0:
        raise ex.SectionException("This section of the board has no more empty tiles. Choose an empty tile anywhere on the board!")
      elif self.board_winners[intended_move] != "":
        raise ex.SectionException(
            "This section of the game has already been decided. Choose an empty tile anywhere on the board!")
    elif next_move != intended_move:
      if self.board_winners[next_move] != "":
        if i_mv_left == 0:
          raise ex.SectionException(
            "This section of the board has no more empty tiles. Choose an empty tile anywhere on the board!")
        return
      if n_mv_left != 0:
        raise ex.SectionException(
            "Based on your opponent's last move, your move is invalid!")
      elif i_mv_left == 0:
        raise ex.SectionException("This section of the board has no more empty tiles. Choose an empty tile anywhere on the board!")
      elif self.board_winners[intended_move] != "":
        raise ex.SectionException(
            "This section of the game has already been decided. Choose an empty tile anywhere on the board!")
  
  ###Issues
  def __ttt_row_check(self, c, r):

    for row in range(c,c+3):
      o_streak = 0
      x_streak = 0
      for col in range(r,r+3):
        cur_char = self.__matrix[row][col]
        if cur_char == "O" and x_streak == 0:
          o_streak += 1
        elif cur_char == "X" and o_streak == 0:
          x_streak += 1
        elif cur_char == "X" and o_streak != 0:
          break
        elif cur_char == "O" and x_streak != 0:
          break
     

      if o_streak == 3:
        return "O"
      elif x_streak == 3:
        return "X"
    return ""
  
  def __ttt_col_check(self, r, c):

    for col in range(c,c+3):
      o_streak = 0
      x_streak = 0
      for row in range(r, r+3):
        cur_char = self.__matrix[row][col]
        if cur_char == "O" and x_streak == 0:
          o_streak += 1
        elif cur_char == "X" and o_streak == 0:
          x_streak += 1
        elif cur_char == "X" and o_streak != 0:
          break
        elif cur_char == "O" and x_streak != 0:
          break

      if o_streak == 3:
        return "O"
      elif x_streak == 3:
        return "X"
    return ""
  
  def __ttt_diag_check(self,r,c):
    d1 = self.__matrix[r][c]
    d2 = self.__matrix[r+1][c+1]
    d3 = self.__matrix[r+2][c+2]

    d4 = self.__matrix[r][c+2]
    d5 = self.__matrix[r+1][c+1]
    d6 = self.__matrix[r+2][c]

    if (d1 == "O" and d2 == "O" and d3 == "O") or (d4 == "O" and d5 == "O" and d6 == "O"):
        return "O"
    elif (d1 == "X" and d2 == "X" and d3 == "X") or (d4 == "X" and d5 == "X" and d6 == "X"):
        return "X"
    return ""

  def __boards_row_check(self,start, end):
    o_streak = 0
    x_streak = 0
    for r in range(start, end):
      winner = self.board_winners["" + str(r)]
      if winner == "O" and x_streak == 0:
        o_streak += 1
      elif winner == "X" and o_streak == 0:
        x_streak += 1
      elif winner == "X" and o_streak != 0:
          break
      elif winner == "O" and x_streak != 0:
          break

    if o_streak == 3:
        return "O"
    elif x_streak == 3:
        return "X"
    return ""
  
  def __boards_cols_check(self, start):
    o_streak = 0
    x_streak = 0
    for c in range(start, start+7,3):
      winner = self.board_winners["" + str(c)]
      if winner == "O" and x_streak == 0:
        o_streak += 1
      elif winner == "X" and o_streak == 0:
        x_streak += 1
      elif winner == "X" and o_streak != 0:
          break
      elif winner == "O" and x_streak != 0:
          break

    if o_streak == 3:
      return "O"
    elif x_streak == 3:
      return "X"
    return ""

  def __boards_diags_check(self):
    d1 = self.board_winners["0"]
    d2 = self.board_winners["4"]
    d3 = self.board_winners["8"]

    d4 = self.board_winners["2"]
    d5 = self.board_winners["4"]
    d6 = self.board_winners["6"]

    if (d1 == "O" and d2 == "O" and d3 == "O") or (d4 == "O" and d5 == "O" and d6 == "O"):
        return "O"
    elif (d1 == "X" and d2 == "X" and d3 == "X") or (d4 == "X" and d5 == "X" and d6 == "X"):
        return "X"
    return ""

  #######Public#######

  def get_tile_symbol(self, row, col):
    return self.__matrix[row][col]

  def print_board(self):
    tb_row = ["    A ", " B ", " C ", "    D ",
              " E ", " F ", "    G ", " H ", " I"]
    horz = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    for i in range(0, len(tb_row)):
      print(tb_row[i], end="")

    print("\n")

    for n in range(0, self.__rows):
      print(horz[n] + "  ", end="")
      for o in range(0, self.__cols):
        if (o + 1 != self.__cols or n + 1 == self.__rows):
          if o == 3 or o == 6:
            print("   ", end="")
          print("|", end="")
          print(self.__matrix[n][o], end="")
          print("|", end="")
        else:
          print("|", end="")
          print(self.__matrix[n][o], end="")
          print("|", end="")
          print("  " + horz[n])
      if n == 2 or n == 5 or n == 8:
        if n == 8:
          print("  " + horz[n], end="")
        print("")

    print("")
    for j in range(0, len(tb_row)):
      print(tb_row[j], end="")

    print("")

  def coord_check(self, coords):
    if self.__matrix[coords[0]][coords[1]] != " ":
      raise ex.CoordException(
          "This tile has already been played on! Please try again!")

  def ttt_check(self, coords):

    x = self.alpha_to_num[coords[0].capitalize()]
    y = self.alpha_to_num[coords[1].capitalize()]

    if x < 3:
      x = 0
    elif x < 6:
      x = 3
    else:
      x = 6

    if y < 3:
      y = 0
    elif y < 6:
      y = 3
    else:
      y = 6

    r = self.__ttt_row_check(y, x)
    c = self.__ttt_col_check(y, x)
    d = self.__ttt_diag_check(y, x)

    board = self.coords_to_board[(y//3, x//3)]

    if c == "O" or r == "O" or d == "O":
      self.board_winners[board] = "O"
      return "O"
    elif c == "X" or r == "X" or d == "X":
      self.board_winners[board] = "X"
      return "X"

    return ""

  def victory_check(self):

    r1 = self.__boards_row_check(0,3)
    r2 = self.__boards_row_check(3,6)
    r3 = self.__boards_row_check(6,9)

    if r1 == "O" or r2 == "O" or r3 == "O":
      return "2"
    elif r1 == "X" or r2 == "X" or r3 == "X":
      return "1"
    
    c1 = self.__boards_cols_check(0)
    c2 = self.__boards_cols_check(1)
    c3 = self.__boards_cols_check(2)

    if c1 == "O" or c2 == "O" or c3 == "O":
      return "2"
    elif c1 == "X" or c2 == "X" or c3 == "X":
      return "1"
    
    d = self.__boards_diags_check()

    if d == "O":
      return "2"
    elif d == "X":
      return "1"

    return ""
  def draw_check(self):
    for i in range(0,9):
      if self.moves_left[str(i)] != 0:
        return False
    return True
  def update_board(self, coords, player, prev_coords):
    try:
      (x1, y1) = (self.alpha_to_num[coords[1].capitalize()], self.alpha_to_num[coords[0].capitalize()])
    except:
      raise ex.CoordException("Invalid Coordinates! Try again!")
    
    try:
      (x2, y2) = (self.alpha_to_num[prev_coords[1].capitalize()], self.alpha_to_num[prev_coords[0].capitalize()])
    except:
      self.coord_check((x1, y1))
      intended_move = self.coords_to_board[(x1//3, y1//3)]
      self.__matrix[x1][y1] = "X"
      self.moves_left[intended_move] -=1
      print("\n")
      self.print_board()
      return
  
    self.coord_check((x1,y1))

    next_move = self.coords_to_board[(x2 % 3, y2 % 3)]

    intended_move = self.coords_to_board[(x1//3, y1//3)]

    self.__valid_board_check(next_move,intended_move)

    if player == "1":
      self.__matrix[x1][y1] = "X"
    else: self.__matrix[x1][y1] = "O"

    self.moves_left[intended_move] -=1
    print("\n")
    self.print_board()
    print("\n")
