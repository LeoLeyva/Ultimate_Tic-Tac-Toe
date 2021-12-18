import exceptions as ex
import random as rd

class State:
  def __init__(self):
    self.last_coordinates = None
    self.cur_player = "1"
    self.usr_player = ""
    self.cur_game = ""
    self.player_choice = False
    self.game_choice = False
    self.ai_v_ai = False
  
  def get_cur_player(self):
    return self.cur_player
  
  def get_usr_player(self):
    return self.usr_player
  
  def get_last_coordinates(self):
    return self.last_coordinates
  
  def get_player_choice(self):
    return self.player_choice
  

  def play(self, coords, bord):
    if self.ai_v_ai:
      raise ex.IllegalCommandException(
          "Select the AI agents that you want to play against each other!")
    if not self.player_choice:
      raise ex.IllegalCommandException("You need to select what player you want to be: 1 or 2?")
    bord.update_board(coords, self.cur_player, self.last_coordinates)
    if self.cur_player == "1":
      self.cur_player = "2"
    else: self.cur_player = "1"
    self.last_coordinates = coords
  
  def player(self, choice):
    if self.ai_v_ai:
      raise ex.IllegalCommandException(
          "Select the AI agents that you want to against each other!")
    if not self.game_choice:
      raise ex.IllegalCommandException(
          "You need to decide which opponent you want to play against!")
    if self.player_choice:
      raise ex.IllegalCommandException("You have already chosen what player you want to be!") 
    elif choice != "1" and choice != "2":
      raise ex.IllegalCommandException(
          "You can only choose to be either player 1 or player 2!")
    else: self.usr_player = choice

    self.player_choice = True
  
  def game(self, choice):
    if self.game_choice:
      raise ex.IllegalCommandException(
          "You have already chosen what game you want to play!")
    elif choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
      raise ex.IllegalCommandException(
          "You can only choose games between 1-5!")
    else: self.cur_game = choice

    self.game_choice = True

  def player_decider(self, fAI, sAI):
    if rd.random() <= 0.5:
      self.cur_ai = fAI
      self.oth_ai = sAI
    else:
      self.cur_ai = sAI
      self.oth_ai = fAI

  def ai_selector(self, choice):
    (x, y) = choice

    if (x != "2" and x != "3" and x != "4") or (y != "2" and y != "3" and y != "4"):
      raise ex.IllegalCommandException(
          "You can only choose between AI options 2, 3, or 4!")
    else:
      self.player_decider(x, y)
