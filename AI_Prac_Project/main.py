import board as bord
import state as stat
import command as cd
import opponent as op

def main():
  instructions()
  start_game()

def instructions():
  print("\nWelcome to our version of Ultimate Tic-Tac-Toe! You will essentially be going against our AI in the fight for supremacy XD.") 
  print("\nThese are the commands and format you are able to use:") 
  print("\n - game <game number 1-5> : this is to select what minigame you want to play (this must be chosen before playing).")
  print("\n - 1 = Human Player, 2= Randomized AI, 3= Heuristic AI, 4= Monte Carlo Tree Search AI, 5= AI vs. AI.")
  print("\n - player <player number 1 or 2> : this is to select whether you want to be player 1 or player 2 (this must be chosen before playing).")
  print("\n - ai <ai number from 2-4><space><,><space><ai number from 2-4> : this is to select what AI agents you want to play against each other (this command can only be entered if you have chosen game 5).")
  print("\n - play <column coordinate><space><,><space><row coordinate> : use this to select a tile to place your symbol on.") 
  print()
  print("\nValid coordinates are written in the following form:  <Letter: A-I or a-i> <,> <Letter:A-I or a -i>.")
  print("\nFor rules on how to play Ultimate Tic-Tac-Toe, visit the following link: https://www.thegamegal.com/2018/09/01/ultimate-tic-tac-toe/\n")


def victory(winner):
  print("Congrats, Playa' " + winner + ", you have won!")


def draw():
  print("Nobody won, but good game!")

def start_game():
  bd = bord.Board()
  bd.print_board()
  prompt(stat.State(),input(),bd)


def prompt(st, str, bd):
  while True:
    try:
      swtch = False
      if st.cur_game != "1" and st.usr_player != "" and st.cur_player != st.usr_player:
        ai = ()
        if st.cur_game == "2":
          ai = op.random_ai(bd, st)
          print("Rand AI: ", end = "")
        elif st.cur_game == "3":
          ai = op.greedy_ai(bd, st)
          print("Heuristic AI: ", end="")
        elif st.cur_game == "4":
          ai = op.montecarlo_ai(bd,st, 100)
          print("MCTS AI: ", end="")
        
        print(ai)

        bd.update_board(ai, st.cur_player, st.last_coordinates)
        st.last_coordinates = ai

        bd.ttt_check(ai)
        res = bd.victory_check()
        if res == "1" or res == "2":
            victory(res)
            return
        if bd.draw_check():
          draw()
          return
        
        if st.cur_player == "1":
          st.cur_player = "2"
        else:
          st.cur_player = "1"
        bd.print_board()
        str = input()
        continue
      action = cd.parse(str)
      if action.command == "play":
        coords = (action.obj_phrase[0], action.obj_phrase[2])
        st.play(coords, bd)
        bd.ttt_check(coords)
        res = bd.victory_check()
      
        if res == "1" or res == "2":
          victory(res)
          return
        
        if bd.draw_check():
          draw()
          return
        bd.print_board()
      elif action.command ==  "player":
        st.player(action.obj_phrase[0])
      elif action.command == "game":
        st.game(action.obj_phrase[0])
      elif action.command == "ai":
        Ais = (action.obj_phrase[0], action.obj_phrase[2])
        st.ai_selector(Ais)
        break
    except IndexError:
      print("Input is not a valid command. Try again!")
    except Exception as e:
      print(e)
      print("berp")
    str = input()
  
  while True:
    ai_move = ()
    if st.cur_ai == "2":
      ai_move = op.random_ai(bd, st)
      print("Rand AI " + st.cur_player + ": ", end="")
    elif st.cur_ai == "3":
      ai_move = op.greedy_ai(bd,st)
      print("Heuristic AI " + st.cur_player + ": ", end="")
    elif st.cur_ai == "4":
      ai_move = op.montecarlo_ai(bd, st, 100)
      print("MCTS AI " + st.cur_player + ": ", end = "")
    print(ai_move)
    bd.update_board(ai_move, st.cur_player, st.last_coordinates)
    bd.print_board()
    st.last_coordinates = ai_move
    bd.ttt_check(ai_move)
    res = bd.victory_check()
    if res == "1" or res == "2":
        victory(res)
        break
    if bd.draw_check():
        draw()
        return
    if st.cur_player == "1":
      st.cur_player = "2"
    else:
        st.cur_player = "1"
    temp = st.cur_ai
    st.cur_ai = st.oth_ai
    st.oth_ai = temp
    




main()
