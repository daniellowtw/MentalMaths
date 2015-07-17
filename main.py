__author__ = 'Daniel'

from Game import Game
from TerminalController import *

# Chooses the GUI to run on
g = Game()
controller = TerminalController(g)
controller.run()
