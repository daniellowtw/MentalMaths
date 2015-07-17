__author__ = 'Daniel'

from enum import Enum

class Operation(Enum):
    ADDITION = 0
    SUBTRACTION = 1
    MULTIPLICATION = 2
    DIVISION = 3

class Question:
    def __hash__(self):
        a = len(str(self.op1))
        b = len(str(self.op2))
        return int(str(2 ** a * 3 ** b) + str(self.op1) + str(self.operation_value) + str(self.op2))

    def __eq__(self, other):
        a = other.op1 == self.op1
        b = other.op2 == self.op2
        c = other.operation_value == self.operation_value
        return all([a, b, c])

    def __init__(self, op1:int, operation_type_value:int, op2:int):
        """
        :param op1: Integer value
        :param operation_type_value: An Operation type value
        :param op2:
        :return:
        """
        self.op1 = op1
        self.op2 = op2
        self.operation_value = operation_type_value
        if operation_type_value == Operation.DIVISION.value:
            op1 *= op2
        self.query = self.get_question_string(op1, operation_type_value, op2)
        self.answer = eval(self.query)
        self.correct_times = []
        self.wrong_times = []

    def add_correct_time(self, time):
        self.correct_times.append(time)

    def add_wrong_time(self, time):
        self.wrong_times.append(time)

    # Print the question
    @staticmethod
    def get_question_string(op1, op_type_value, op2):
        symbol = list("+-*/")
        return "%i %s %i\n" % (op1, symbol[op_type_value], op2)