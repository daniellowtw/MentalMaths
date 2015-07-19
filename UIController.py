__author__ = 'Daniel'

from enum import Enum


class AbstractController:
    """
    An abstract class for a controller to the game
    """

    class QuestionAction(Enum):
        QUIT = 'q'
        SAVE = 's'

    class Action(Enum):
        SET_LIMIT = 'l'
        START = 's'
        QUIT = 'q'
        HISTORY = 'h'
        TRAINING = 't'

    def __init__(self, game):
        self.game = game

    def run(self):
        raise NotImplementedError
