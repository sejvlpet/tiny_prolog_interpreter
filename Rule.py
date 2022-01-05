from abc import ABC, abstractmethod
from Clause import Clause
from Constatnts import *

class Rule(Clause):

    def __init__(self, head, body):
        splitted_head = head.split(CLAUSE_START)

        # fixme this should rather be new object, predicate or something like that
        self._name = splitted_head[0]
        self._params = splitted_head[1].split(CLAUSE_END)[0].split(ATOM_SEPARATOR)
        self._cutting = False # default value
        super().__init__(body)


    """ from string creates value of the fact"""
    def _get_value(self, body):
        splitted = body.strip().split(PREDICATE_SEPARATOR)

        if splitted[-1] != CUT_SIGN:
            # to keep things consitent, remove last paranthesis
            splitted[-1] = splitted[-1][: -len(CLAUSE_END)]
            self._cutting = False # just for sure
        else:
            self._cutting = True


        return splitted

    """ test method """
    def compare_name_value(self, name, value, params, cutting):
        if len(value) != len(self._value):
            return False

        for i in range(len(value)):
            if value[i] != self._value[i]:
                return False

        for i in range(len(params)):
            if params[i] != self._params[i]:
                return False

        return name == self._name and cutting == self._cutting