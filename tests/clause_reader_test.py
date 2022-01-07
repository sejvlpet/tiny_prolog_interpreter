import unittest
from main.clause.clause_reader import Clause_reader
from main.question.is_question import Is_question
from main.question.custom_question import Custom_question

"""
Tests thing around clauses
"""

class TestClause(unittest.TestCase):
    def setUp(self):
        pass

    def test_clause_reader_basic(self):
        line = "parent(a,b,1,2)"
        reader = Clause_reader(line)
        res = reader.read()
        self.assertTrue(res.compare_name_value("parent", ["a", "b", 1, 2], False))


    def test_clause_reader_basic_cutting(self):
        line = "parent(a,b,1,2):-!"
        reader = Clause_reader(line)
        res = reader.read()
        self.assertTrue(res.compare_name_value("parent", ["a", "b", 1, 2], True))


    def test_clause_reader_variable(self):
        line = "parent(X,b,1,2):-!"
        reader = Clause_reader(line)

        try:
            res = reader.read()
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def test_clause_reader_weid_input(self):
        line = "parent(a,b,1,2dsdf)sfsdf-sdf"
        reader = Clause_reader(line)

        try:
            res = reader.read()
            self.assertTrue(False)
        except:
            self.assertTrue(True)


    def test_clause_reader_rule_custom_question(self):
        line = "tra(X,Z):-tra(X,Y),tra(Y,Z)"
        reader = Clause_reader(line)
        res = reader.read()

        self.assertTrue(res.compare_name_value("tra", [Custom_question("tra(X,Y)"),
                                                    Custom_question("tra(Y,Z)")],
                                                    ["X", "Z"],
                                                    False))

    def test_clause_reader_rule_is_question(self):
        line = "tra(X,Z):-10is5*2"
        reader = Clause_reader(line)
        res = reader.read()

        self.assertTrue(res.compare_name_value("tra", [Is_question(10, 5, 2, "*")], ["X", "Z"],
                                                    False))


    def test_clause_reader_rule_is_question_cutting(self):
        line = "tra(X,Z):-10is5*2,!"
        reader = Clause_reader(line)
        res = reader.read()

        self.assertTrue(res.compare_name_value("tra", [Is_question(10, 5, 2, "*")], ["X", "Z"],
                                                    True))



    def test_clause_reader_rule_all(self):
        line = "tra(X,Z):-tra(X,Y),tra(Y,Z),10is5*2,!"
        reader = Clause_reader(line)
        res = reader.read()

        self.assertTrue(res.compare_name_value("tra", [Custom_question("tra(X,Y)"),
                                                    Custom_question("tra(Y,Z)"), Is_question(10, 5, 2, "*")],
                                               ["X", "Z"],
                                                    True))


if __name__ == '__main__':
    unittest.main()
