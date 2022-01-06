import unittest
from main.clause.Clause_reader import Clause_reader

"""
Tests thing around clauses
"""

class TestClause(unittest.TestCase):
    def setUp(self):
        pass

    def test_clause_reader_basic(self):
        line = "parent(a, b, 1, 2)"
        reader = Clause_reader(line)
        res = reader.read()
        self.assertTrue(res.compare_name_value("parent", ["a", "b", 1, 2], False))


    def test_clause_reader_basic_cutting(self):
        line = "parent(a, b, 1, 2) :-       ! "
        reader = Clause_reader(line)
        res = reader.read()
        self.assertTrue(res.compare_name_value("parent", ["a", "b", 1, 2], True))


    def test_clause_reader_variable(self):
        line = "parent(X, b, 1, 2) :-       ! "
        reader = Clause_reader(line)

        try:
            res = reader.read()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_clause_reader_weid_input(self):
        line = "parent(a, b, 1, 2dsdf) sfsdf:- sdf"
        reader = Clause_reader(line)

        try:
            res = reader.read()
            self.assertTrue(False)
        except:
            self.assertTrue(True)


    def test_clause_reader_rule_basic(self):
        line = "tra(X, Z) :- tra(X, Y), tra(Y, X)"
        reader = Clause_reader(line)
        res = reader.read()

        print("olalala")





if __name__ == '__main__':
    unittest.main()
