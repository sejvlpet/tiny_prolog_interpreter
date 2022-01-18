import unittest
from clause.fact import Fact
from clause.rule import Rule
from database import Database

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
                    Rule("fact(N, Res)".replace(" ", ""), "X is N - 1&fact(X, TMP)&Res is N * TMP".replace(" ", ""))
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

        expected = [{'X': 1}], False

        self.assertEqual(database.answer(name, body), expected)

    def test_contains_fact_fill_ok2(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        body = ['A', 'B']

        expected = [{'A': 0, 'B': 1}], False

        self.assertEqual(database.answer(name, body), expected)

    def test_simple_rule_true(self):
        file_path = "test_files/load2"
        database = Database(file_path)
        name = "fact"
        body = [0, 1]

        self.assertEqual(database.answer(name, body), (True, False))

    def test_simple_rule_true2(self):
        file_path = "test_files/load2"
        database = Database(file_path)
        name = "test"
        body = [10, 7, 3]

        self.assertEqual(database.answer(name, body), (True, False))

    def test_simple_rule_false(self):
        file_path = "test_files/load2"
        database = Database(file_path)
        name = "fact"
        body = [1, 1]

        self.assertEqual(database.answer(name, body), (False, False))

    def test_simple_rule_false2(self):
        file_path = "test_files/load2"
        database = Database(file_path)
        name = "test"
        body = [11, 7, 3]

        self.assertEqual(database.answer(name, body), (False, False))

    def test_check_fact_6(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        body = [6, "X"]

        expected = [{'X': 720}], False

        self.assertEqual(database.answer(name, body), expected)

    def test_check_fib(self):
        file_path = "test_files/load3"
        database = Database(file_path)
        name = "fib"
        body = [6, "X"]

        expected = [{'X': 13}], False

        self.assertEqual(database.answer(name, body), expected)

    def test_fact_up_to_100(self):
        f = 1
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        for i in range(1, 100):
            f *= i
            body = [i, 'X']
            self.assertEqual(f, database.answer(name, body)[0][0]['X'])

    def test_fib_up_to_20(self):
        f = [1, 1]
        file_path = "test_files/load3"
        database = Database(file_path)
        name = "fib"
        for i in range(1, 20):
            f.append(f[-1] + f[-2])
            body = [i, 'X']
            self.assertEqual(f[i], database.answer(name, body)[0][0]['X'])

    def test_multiple_fact_fill(self):
        file_path = "test_files/load3"
        database = Database(file_path)
        name = "fib"
        body = ["A", 1]
        expc1 = ([{'A': 0}, {'A': 1}], False)

        self.assertEqual(expc1, database.answer(name, body))

        body2 = ["A", "B"]
        expc2 = ([{'A': 0, 'B': 1}, {'A': 1, 'B': 1}], False)
        self.assertEqual(expc2, database.answer(name, body2))

    def test_multiple_rule_fill(self):
        file_path = "test_files/load4"
        database = Database(file_path)
        name = "fact"
        body = [5, "N"]

        excp = ([{'N': 50}, {'N': 120}], False)
        self.assertEqual(excp, database.answer(name, body))


    def test_cutting_rule(self):
        file_path = "test_files/load5"
        database = Database(file_path)
        name = "fact"
        body = [5, "N"]

        excp = ([{'N': 50}], False)
        self.assertEqual(excp, database.answer(name, body))

    def test_fact_check(self):
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        body = [5, 120]

        expected = (True, False)
        self.assertEqual(database.answer(name, body), expected)

    def test_fact_up_to_100_check(self):
        f = 1
        file_path = "test_files/load1"
        database = Database(file_path)
        name = "fact"
        for i in range(1, 100):
            f *= i
            body = [i, f]

            expected = (True, False)
            self.assertEqual(expected, database.answer(name, body))

    def test_fib_up_to_20_check(self):
        f = [1, 1]
        file_path = "test_files/load3"
        database = Database(file_path)
        name = "fib"
        for i in range(1, 20):
            f.append(f[-1] + f[-2])
            body = [i, f[i]]

            expected = (True, False)
            self.assertEqual(expected, database.answer(name, body))

if __name__ == '__main__':
    unittest.main()
