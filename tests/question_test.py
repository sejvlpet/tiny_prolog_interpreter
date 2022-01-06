import unittest
from main.question.is_question import Is_question

"""
Tests thing around question
"""

class TestClause(unittest.TestCase):
    def setUp(self):
        pass

    def test_is_question_val_ok_plus(self):
        q = Is_question(10, 8, 2, "+")
        a = q.answer()
        self.assertTrue(a)

    def test_is_question_val_ok_prod(self):
        q = Is_question(16, 8, 2, "*")
        a = q.answer()
        self.assertTrue(a)

    def test_is_question_val_fail_plus(self):
        q = Is_question(16, 8, 2, "+")
        a = q.answer()
        self.assertFalse(a)

    def test_is_question_val_fail_prod(self):
        q = Is_question(26, 8, 2, "*")
        a = q.answer()
        self.assertFalse(a)

    def test_is_question_val_plus(self):
        q = Is_question(None, 8, 2, "+")
        a = q.answer()
        self.assertTrue(a == 10)

    def test_is_question_val_prod(self):
        q = Is_question(None, 8, 4, "*")
        a = q.answer()
        self.assertTrue(a == 32)

    def test_is_question_one_ok(self):
        q = Is_question(10, 10)
        a = q.answer()
        self.assertTrue(a)

    def test_is_question_one_val(self):
        q = Is_question(None, 10)
        a = q.answer()
        self.assertTrue(a == 10)

    def test_is_question_one_val_fail(self):
        q = Is_question(11, 12)
        a = q.answer()
        self.assertFalse(a)

    # todo custom_question tests


if __name__ == '__main__':
    unittest.main()
