import unittest
from Clause_reader import Clause_reader

"""
Tests thing around clauses
"""

class TestClause(unittest.TestCase):
    def setUp(self):
        pass

    def test_clause_reader_basic(self):
        line = "parent(a, b, 1, 2)."
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
        line = "parent(X, b, 1, 2dsdf) sfsdf:- sdf"
        reader = Clause_reader(line)

        try:
            res = reader.read()
            self.assertTrue(False)
        except:
            self.assertTrue(True)





if __name__ == '__main__':
    unittest.main()
