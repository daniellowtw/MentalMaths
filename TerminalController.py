__author__ = 'Daniel'

# Responsible for generating UI in terminal

import os
from UIController import AbstractController
from utility import *
from question import Operation
from UserData import config


class InterruptInputException(Exception):
    def __init__(self, msg):
        self.msg = msg


class TerminalController(AbstractController):
    game = None

    def get_user_input_for_question(self, query, allowed_operations=[]):
        """
        Converts the user input into a float to check whether the input is correct. If that is not possible, this
        will keep retrying.
        """
        try:
            user_input = input(query)
            if str.isalpha(user_input):
                if user_input in map(lambda x: x.value, allowed_operations):
                    if TerminalController.QuestionAction.SAVE.value == user_input:
                        self.game.save_current_question()
                        print("Saved")
                    elif self.QuestionAction.QUIT.value == user_input:
                        raise InterruptInputException(TerminalController.QuestionAction(user_input))
            else:
                return float(user_input)
        except ValueError as e:
            print(e)
        return self.get_user_input_for_question(query, allowed_operations)

    def __init__(self, game):
        self.game = game

    def play_round_wrapper(self, question_generator):
        rounds = get_integer_input("Enter number of rounds (leave empty for 10): ", 10)
        score, total = self.play_round(rounds, question_generator)
        print("Round completed. %i / %i" % (score, total))
        self.game.user_score.save_db()
        return

    def play_round(self, number_of_rounds, question_generator):
        score = 0
        total = 0
        os.system('cls' if os.name == 'nt' else 'clear')
        for _ in range(number_of_rounds):
            question_generator()
            self.game.start_timing()
            try:
                user_input = self.get_user_input_for_question(self.game.current_question.query,
                                                              [TerminalController.QuestionAction.QUIT,
                                                               TerminalController.QuestionAction.SAVE])
            except InterruptInputException as e:
                if e.msg == TerminalController.QuestionAction.QUIT:
                    print("Returning to main menu.")
                    return score, total
                elif e.msg == TerminalController.QuestionAction.SAVE:
                    self.game.save_current_question()
            self.game.end_timing()
            outcome, correct_value, time_taken = self.game.solve_question(user_input)
            if config.getboolean("General", "SHOW_TIMER"):
                print("Time taken:" + str(time_taken))
            total += 1
            if outcome:
                score += 1
                print("Correct!")
            else:
                print("Wrong, correct value is %i" % correct_value)
            if config.getboolean("General", "PAUSE_AFTER_QUESTION"):
                user_input = input("Enter any key to continue. S to save the question, Q to quit")
                if str.isalpha(user_input):
                    if TerminalController.QuestionAction.SAVE.value == user_input:
                        self.game.save_current_question()
                    elif TerminalController.QuestionAction.QUIT.value == user_input:
                        return score, total
        return score, total

    def run(self):
        while True:
            self.menu_main()

    def menu_main(self):
        instruction = """
q - Quit
l - Set limit
s - Start game
h - History
t - Training
"""
        print(instruction)
        input_string = input("Please enter command:")
        if input_string == self.Action.START.value:
            self.play_round_wrapper(self.game.gen_next_question)
        elif input_string == self.Action.QUIT.value:
            exit()
        elif input_string == self.Action.SET_LIMIT.value:
            lower = int(input("Enter lower limit (inclusive): "))
            upper = int(input("Enter upper limit (inclusive): "))
            self.game.lower = lower
            self.game.upper = upper
        elif input_string == self.Action.HISTORY.value:
            print("\n%s %s / %s" % ("Query".ljust(10), "R".ljust(4), "W".ljust(4)))
            for q in self.game.history.values():
                print("%s %s / %s" % (q.query.strip().ljust(10, ' '), str(len(q.correct_times)).ljust(4, ' '),
                                      str(len(q.wrong_times)).ljust(4, ' ')))
        elif input_string == self.Action.TRAINING.value:
            self.menu_training()
        else:
            print("unknown command")

    def menu_training(self):
        instruction = """
1 - Squaring
2 - Multiplying two numbers having the same first n-1 digits and ones digit add up to ten
3 - Multiplying two numbers ending with 1
4 - Multiplication within a range
5 - Addition within a range
6 - Subtraction within a range
7 - Division within a range
8 - Multiplying two numbers having the first n-1 digits

0 - Go back
"""
        print(instruction)
        choice = get_integer_input("Enter a number: ")
        if choice == 0:
            return
        elif choice == 1:
            lower_bound = get_integer_input("Enter a lower bound (leave empty for 1): ", 1)
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 99): ", 99)
            self.play_round_wrapper(lambda: self.game.gen_squares(lower_bound, upper_bound))
        elif choice == 2:
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 9): ", 99)
            self.play_round_wrapper(lambda: self.game.gen_ones_digit_sum_to_ten(upper_bound))
        elif choice == 3:
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 9): ", 9)
            self.play_round_wrapper(lambda: self.game.gen_numbers_ending_with_one(upper_bound))
        elif choice == 4:
            lower_bound = get_integer_input("Enter a lower bound (leave empty for 1): ", 1)
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 99): ", 99)
            self.play_round_wrapper(
                lambda: self.game.gen_next_question(lower_bound, upper_bound, Operation.MULTIPLICATION.value))
        elif choice == 5:
            lower_bound = get_integer_input("Enter a lower bound (leave empty for 100): ", 100)
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 999): ", 999)
            self.play_round_wrapper(
                lambda: self.game.gen_next_question(lower_bound, upper_bound, Operation.ADDITION.value))
        elif choice == 6:
            lower_bound = get_integer_input("Enter a lower bound (leave empty for 1): ", 1)
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 999): ", 999)
            self.play_round_wrapper(
                lambda: self.game.gen_next_question(lower_bound, upper_bound, Operation.SUBTRACTION.value))
        elif choice == 7:
            lower_bound = get_integer_input("Enter a lower bound (leave empty for 1): ", 1)
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 99): ", 99)
            self.play_round_wrapper(
                lambda: self.game.gen_next_question(lower_bound, upper_bound, Operation.DIVISION.value))
        elif choice == 8:
            upper_bound = get_integer_input("Enter an upper bound (leave empty for 9): ", 9)
            self.play_round_wrapper(lambda: self.game.gen_tens_digit_are_the_same(upper_bound))
        else:
            self.menu_training()
