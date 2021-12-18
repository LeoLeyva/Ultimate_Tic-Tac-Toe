from board import Board
from state import State
import command as cd
import opponent as op

def experiment (ai1,ai2,n):
  one = 0
  two = 0
  draw = 0
  for i in range(0,n):
    st = State()
    st.cur_ai = ai1
    st.oth_ai = ai2
    bd =  Board()
    while True:
      ai_move = ()
      if st.cur_ai == "2":
        ai_move = op.random_ai(bd, st)
      # elif st.cur_ai == "3":
      #   ai_move =
      #   print("Heuristic AI " + st.cur_player + ": ", end="")
      # elif st.cur_ai == "4":
      #   ai_move =
      #   print("MCTS " + st.cur_player + ": ", end = "")
      bd.update_board(ai_move, st.cur_player, st.last_coordinates)
      st.last_coordinates = ai_move
      bd.ttt_check(ai_move)
      res = bd.victory_check()
      if res == "1":
        one+=1
        break
      elif res == "2":
        two +=1 
        break
      if bd.draw_check():
        draw+=1
        break
      if st.cur_player == "1":
        st.cur_player = "2"
      else:
          st.cur_player = "1"
      temp = st.cur_ai
      st.cur_ai = st.oth_ai
      st.oth_ai = temp
  
  print("First AI: " + str(one))
  print("Second AI: " + str(two))
  print("Draw: " + str(draw))

experiment(input(),input(),1000)
