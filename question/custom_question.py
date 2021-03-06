from question.question import Question
from constatnts import *

class Custom_question(Question):
    """ Fact_question simply checks the database"""
    def __init__(self, clause):
        splitted = clause.split(CLAUSE_START)
        self._name = splitted[0].strip()
        self._body = splitted[1].split(CLAUSE_END)[0].split(ATOM_SEPARATOR)
        self._fix_types()

    def name(self):
        return self._name

    def body(self):
        return self._body

    def __eq__(self, other):
        if len(self._body) != len(other._body):
            return False
        for i in range(len(self._body)):
            if self._body[i] != other._body[i]:
                return False
        return self._name == other._name


    def answer(self, answerer):
        return answerer.answer(self._name, self._body)

    def _fix_types(self):
        new_body = []
        for tmp in self._body:
            if tmp.isdigit():
                new_body.append(int(tmp))
            else:
                new_body.append(tmp)
        self._body = new_body