import unittest
from main.clause.clause_reader import Clause_reader
from main.question.is_question import Is_question
from main.question.custom_question import Custom_question
from main.clause.fact import Fact
from main.clause.rule import Rule
from main.database import Database
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
                    Rule("fact(N, Res)".replace(" ", ""), "N1 is N - 1&fact(N1, SubRes)&Res is N * SubRes&!".replace(" ", ""))
                ]
            },
            "tra": {
                2: [
                    Rule("tra(X, Y)".replace(" ", ""), "tra(X, Z)& tra(Z, Y)".replace(" ", ""))
                ]
            }
        }

        self.assertEqual(expected_result["fact"][2][0], c["fact"][2][0])
        self.assertEqual(expected_result["fact"][2][1], c["fact"][2][1])
        self.assertEqual(expected_result["tra"][2][0], c["tra"][2][0])

    def test_contains_fact_true(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        fact = Fact("fact(0, 1).", False)

        self.assertEqual(database.answer(fact.name(), fact._value), (True, False))

    def test_contains_fact_false(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        fact = Fact("fact(0, 2).", False)

        self.assertEqual(database.answer(fact.name(), fact._value), (False, False))

    def test_contains_fact_fill_ok(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        body = [0, "X"]

        expected = [{'X': 1}]

        self.assertEqual(database.answer(name, body), expected)

    def test_contains_fact_fill_ok2(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        body = ['X', 'Y']

        expected = [{'X': 0, 'Y': 1}]

        self.assertEqual(database.answer(name, body), expected)

    def test_contains_fact_fill_notok(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        body = [1, "X"]

        expected = []

        self.assertEqual(database.answer(name, body), expected)


    def test_simple_rule_true(self):
        file_path = "test_files/load2"
        database = Database(file_path)
        name = "fact"
        body = [0, 1]

        self.assertEqual(database.answer(name, body), (True, False))

    def test_simple_rule_false(self):
        file_path = "test_files/load2"
        database = Database(file_path)
        name = "fact"
        body = [1, 1]

        self.assertEqual(database.answer(name, body), (False, False))

if __name__ == '__main__':
    unittest.main()
