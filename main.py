__author__ = 'Daniel'
__version__ = '0.0.2'

from Game import Game
from TerminalController import *
from game_controller import *

# Chooses the GUI to run on
g = Game()
controller = TerminalController(g)
controller = QtController(g)
controller.run()
