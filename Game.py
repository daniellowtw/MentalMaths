__author__ = 'Daniel'

from random import randint, randrange
from Question import *
from time import clock
from UserData import *


class UnknownCommandException(Exception):
    def __init__(self, msg):
        self._msg = msg


class NoQuestionException(Exception):
    pass


class Game:
    """
    Represents a game instance

    Recommended training questions based on the following
    1) Squaring a number
    2) Multiplying two numbers having the same first n-1 digits and ones digit add up to ten
    3) Multiplying two numbers ending with 1
    4) Multiplication between a range
    """

    def __init__(self):
        self.lower = 0
        self.upper = 100
        self.score = 0
        self.total_questions = 0
        self.current_question = None
        self.history = {}
        self.user_score = None
        self.saved_question = []
        self.start_time = 0
        self.end_time = 0
        self.set_history()

    def set_history(self):
        """
        Loads history from database
        :return:
        """
        self.user_score = UserData()
        self.user_score.load_or_create_db()
        self.history = self.user_score.db

    def start_timing(self):
        self.start_time = clock()

    def end_timing(self):
        self.end_time = clock()

    def save_current_question(self):
        self.saved_question.append(self.current_question)

    def gen_next_question(self, lower=None, upper=None, op_type_value=None):
        """
        Generate a random question based on the given parameter (if any)
        :param lower:
        :param upper:
        :param op_type_value:int Give the operation value
        :return:
        """

        lower_bound = self.lower if lower is None else lower
        upper_bound = self.upper if upper is None else upper
        op1 = randint(lower_bound, upper_bound)
        op2 = randint(lower_bound, upper_bound)
        if op_type_value is None:
            op_type_value = randrange(len(Operation))
        self.current_question = Question(op1, op_type_value, op2)

    def solve_question(self, user_input):
        """
        Take a user input and check whether it solves the current question
        :param user_input:
        :return:
        """
        if self.current_question is None:
            raise NoQuestionException
        time_taken = self.end_time - self.start_time
        solution = eval(self.current_question.query)
        is_user_correct = solution == user_input
        self.total_questions += 1
        if hash(self.current_question) in self.history:
            self.current_question = self.history[hash(self.current_question)]
        if is_user_correct:
            self.score += 1
            self.current_question.add_correct_time(time_taken)
        else:
            self.current_question.add_wrong_time(time_taken)
        self.history[hash(self.current_question)] = self.current_question

        # For displaying purposes
        return is_user_correct, solution, time_taken

    def gen_squares(self, lower, upper):
        """
        Generate a square question between range upper and lower inclusive
        :param lower:
        :param upper:
        :return:
        """
        x = randint(lower, upper)
        self.current_question = Question(x, Operation.MULTIPLICATION.value, x)

    def gen_ones_digit_sum_to_ten(self, upper_bound):
        """
        two numbers having the same first n-1 digits and ones digit add up to ten
        :param upper_bound:
        :return:
        """
        ones = randint(1, 9)
        ones_complement = 10 - ones
        tens1 = randint(1, upper_bound)
        self.current_question = Question(tens1 * 10 + ones, Operation.MULTIPLICATION.value,
                                         upper_bound * 10 + ones_complement)

    def gen_tens_digit_are_the_same(self, upper_bound):
        """
        Generate two numbers with the same first n-1 digits and is <= upperbound
        :param upper_bound:
        :return:
        """
        ones1 = randint(0, 9)
        ones2 = randint(0, 9)
        tens = randint(upper_bound)
        self.current_question = Question(tens * 10 + ones1, Operation.MULTIPLICATION.value, tens * 10 + ones2)

    def gen_numbers_ending_with_one(self, upper_bound):
        """
        Generate two numbers ending with one with the first n-1 digit <= upper_bound
        :param upper_bound:
        :return:
        """
        tens1 = randint(upper_bound)
        tens2 = randint(upper_bound)
        self.current_question = Question(tens1 * 10 + 1, Operation.MULTIPLICATION.value, tens2 * 10 + 1)
