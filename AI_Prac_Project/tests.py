import unittest
from board import Board
import board as bd
import exceptions as ex
import state
import command

class TestBoardMethods(unittest.TestCase):
  bd1 = Board()
  try:
    for i in range(0,9):
      for j in range(0,9):
        bd1.coord_check((i, j))
  except:
    print("The tiles are somehow not" + 
      " all empty at the start.")
  
  bd2 = Board()
  bd2.update_board(("A", "A"),"2", None)


# class TestCommandMethods(unittest.TestCase):

# class TestStateMethods(unittest.TestCase):


if __name__ == '__main__':
    unittest.main()
