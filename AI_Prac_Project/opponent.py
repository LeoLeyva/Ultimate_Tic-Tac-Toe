import random as rd

def possible_moves(bd, st):
  ans = []
  alpha = ["A","B","C","D","E","F","G","H","I"]
  if st.last_coordinates == None:
    for i in range(0,len(alpha)):
      for j in range (0,len(alpha)):
        ans.append((alpha[i],alpha[j]))
    return ans
  
  (x2, y2 ) = st.last_coordinates
  (x2, y2) = (bd.alpha_to_num[x2.capitalize()] %
              3, bd.alpha_to_num[y2.capitalize()] % 3)
  next_move = bd.coords_to_board[(y2 ,x2)]

  print(bd.coords_to_board[(y2, x2)])
  if bd.moves_left[next_move] == 0 or bd.board_winners[next_move] != "":
    for i in range(0, len(alpha)):
      for j in range(0, len(alpha)):
        next_move = bd.coords_to_board[(j % 3, i % 3)]
        if bd.moves_left[next_move] == 0 or bd.board_winners[next_move] != "":
          continue
        if bd.get_tile_symbol(i, j) == " ":
          ans.append((alpha[j], alpha[i]))
    return ans
  
  (x2,y2) = (x2*3,y2*3)
  
  for row in range(y2, y2+3):
      for col in range(x2, x2+3):
        if bd.get_tile_symbol(row,col) == " ":
          ans.append((alpha[col], alpha[row]))
  
  return ans

def random_ai(bd, st):
  pos = possible_moves(bd,st)
  print(pos)
  return pos[rd.randrange(0,len(pos))]
#------------------------
def greedy_ai():
  return



#------------------------
def montecarlo_ai():
  return
