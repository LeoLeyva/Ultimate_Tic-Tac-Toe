import exceptions as ex
import random as rd

class Aistate:
  def __init__(self):
    self.last_coordinates = None
    self.cur_player = "1"
    self.cur_ai = ""
    self.oth_ai = ""
    self.ai_choice = False

  def get_cur_player(self):
    return self.cur_player

  def get_last_coordinates(self):
    return self.last_coordinates

  def player_decider(self, fAI, sAI):
    if rd.random() <= 0.5 :
      self.cur_ai = fAI
      self.oth_ai = sAI
    else: 
      self.cur_ai = sAI
      self.oth_ai = fAI

  def play(self, coords, bord):
    if not self.player_choice:
      raise ex.IllegalCommandException(
          "You need to select what player you want to be: 1 or 2?")
    bord.update_board(coords, self.cur_player, self.last_coordinates)
    if self.cur_player == "1":
      self.cur_player = "2"
    else:
      self.cur_player = "1"
    self.last_coordinates = coords

  def aiselector(self, choice):
    (x,y) = choice

    if (x != "1" and x != "2" and x != "3") or (y != "1" and y != "2" and y != "3"):
      raise ex.IllegalCommandException(
          "You can only choose between AI options 1, 2, or 3!")
    else:
      self.player_decider(x,y)
