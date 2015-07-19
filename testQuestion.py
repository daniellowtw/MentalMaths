__author__ = 'Daniel'

import unittest
from question import *


class TestQuestionMethods(unittest.TestCase):
    def test_question_creation(self):
        q = Question(1, Operation.ADDITION.value, 2)
        self.assertEqual(q.op1, 1)
        self.assertEqual(q.op2, 2)
        self.assertEqual(q.type, Operation.ADDITION.value)

    def test_question_hash(self):
        q1 = Question(1, Operation.ADDITION.value, 2)
        q2 = Question(1, Operation.ADDITION.value, 2)
        q1.add_correct_time(1)
        q2.add_correct_time(2)
        self.assertEqual(hash(q1), hash(q2))
        self.assertEqual(q1, q2)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestQuestionMethods.suite())
    return test_suite

if __name__ == '__main__':
    unittest.main()
