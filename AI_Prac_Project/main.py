from typing import ForwardRef
import board as bord
import state as stat
import command as cd

def main():
  instructions()
  start_game()

def instructions():
  print("\nWelcome to our version of Ultimate Tic-Tac-Toe! You will essentially be going against our AI in the fight for supremacy XD.") 
  print("\nThese are the commands and format you are able to use:") 
  print("\n - play <column coordinate><space><,><space><row coordinate> : use this to select a tile to place your symbol on.") 
  print("\n - player <player number 1 or 2> : this is to select whether you want to be player 1 or player 2 (this can only be chosen in the beginning).") 
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
      action = cd.parse(str)
      if action.command == "play":
        coords = (action.obj_phrase[0], action.obj_phrase[2])
        st.play(coords, bd)
        bd.ttt_check(coords)
        res = bd.victory_check()
        print(res)
        if res == "1" or res == "2":
          victory(res)
          break
      elif action.command ==  "player":
        st.player(action.obj_phrase[0])
    except Exception as e:
      print(e)
    str = input()




main()