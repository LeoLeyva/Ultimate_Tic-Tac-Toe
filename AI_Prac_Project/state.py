import board as bd
import exceptions as ex

class State:
  def __init__(self):
    self.last_coordinates = None
    self.cur_player = "1"
    self.usr_player = ""
    self.player_choice = False
  
  def get_cur_player(self):
    return self.cur_player
  
  def get_usr_player(self):
    return self.usr_player
  
  def get_last_coordinates(self):
    return self.last_coordinates
  
  def get_player_choice(self):
    return self.player_choice
  

  def play(self, coords, bord):
    if not self.player_choice:
      raise ex.IllegalCommandException("You need to select what player you want to be: 1 or 2?")
    bord.update_board(coords, self.cur_player, self.last_coordinates)
    if self.cur_player == "1":
      self.cur_player = "2"
    else: self.cur_player = "1"
    self.last_coordinates = coords
  
  def player(self, choice):
    if self.player_choice:
      raise ex.IllegalCommandException("You have already chosen what player you want to be!") 
    elif choice != "1" and choice != "2":
      raise ex.IllegalCommandException(
          "You can only choose to be either player 1 or player 2!")
    else: self.usr_player = choice

    self.player_choice = True
