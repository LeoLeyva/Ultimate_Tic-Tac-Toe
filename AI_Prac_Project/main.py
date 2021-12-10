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
  print("\n - play <column coordinate><space><,><space><row coordinate> : use this to select a tile to place your symbol on.") 
  print("\n - player <player number 1 or 2> : this is to select whether you want to be player 1 or player 2 (this can only be chosen in the beginning).") 
  print()
  print("\nValid coordinates are written in the following form:  <Letter: A-I or a-i> <,> <Letter:A-I or a -i>.")
  print("\nFor rules on how to play Ultimate Tic-Tac-Toe, visit the following link: https://www.thegamegal.com/2018/09/01/ultimate-tic-tac-toe/\n")


def victory( winner):
  print("Congrats, Player " + winner + ", you have won!")

def start_game():
  bd = bord.Board()
  bd.print_board()
  prompt(stat.State(),input(),bd)


def prompt(st, str, bd):
  vic = False
  while True:
    try:
      swtch = False
      if swtch and st.usr_player != "" and st.cur_player != st.usr_player:
        if st.cur_game == "2":
          rd = op.random_ai(bd, st)
          print(rd)
          bd.update_board(rd, st.cur_player, st.last_coordinates)
          st.last_coordinates = rd
        
          bd.ttt_check(rd)
          res = bd.victory_check()
          if res == "1" or res == "2":
            victory(res)
            break

        if st.cur_player == "1":
          st.cur_player = "2"
        else:
          st.cur_player = "1"
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
          break
        
        # if (st.cur_game != "1"):
        #   if(st.cur_game == "2"):
        #   elif (st.cur_game == "3":
        #   elif (st.cur_game == "4"):
          
        #   str = input()
      elif action.command ==  "player":
        st.player(action.obj_phrase[0])
      elif action.command == "game":
        st.game(action.obj_phrase[0])
    except IndexError:
      print("Input is not a valid command. Try again!")
    except Exception as e:
      print(e)
      print("berp")
    str = input()




main()
