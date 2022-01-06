from main.question.question import Question
from main.constatnts import *

""" Fact_question simply checks the database"""
class Custom_question(Question):

    def __init__(self, clause, database):
        splitted = clause.split(CLAUSE_START)
        self._name = splitted[0]
        self._body = splitted[1].split(CLAUSE_END)[0]
        self._database = database

    def answer(self):
        if self._is_fact():
            return self._database.contains_fact(self._name, self._body)

        return self._database.satisfies_rule(self._name, self._body)

    def _is_fact(self):
        for a in self._body:
            if not is_atom(a):
                return False

        return True
