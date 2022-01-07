import unittest
from main.clause.clause_reader import Clause_reader
from main.question.is_question import Is_question
from main.question.custom_question import Custom_question
from main.clause.fact import Fact
from main.clause.rule import Rule
from main.database import Database
import deepdiff
"""
Tests thing around clauses
"""

class TestClause(unittest.TestCase):
    def setUp(self):
        pass

    def test_load_from_file(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        c = database.clauses()

        expected_result = {
            "fact": {
                2: [
                    Fact("fact(0, 1).", False),
                    Rule("fact(N, Res)", "N1 is N - 1&fact(N1, SubRes)&Res is N * SubRes&!")
                ]
            },
            "tra": {
                2: [
                    Rule("tra(X, Y)", "tra(X, Z), tra(Z, Y)")
                ]
            }
        }

        self.assertTrue(c == expected_result)

if __name__ == '__main__':
    unittest.main()
