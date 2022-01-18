from abc import ABC, abstractmethod
from constatnts import *


class Clause(ABC):
    """
    Abstract parent to clauses

    We shall differentiate between two types of clauses, rule and fact.
    Fact is always true a can be either final (meaning it does cut (!)), or not. Only atoms in fact definition are allowed
    Rule is true if it's body is true, body can consist from other clauses and questions.
    """
    def __init__(self, body, name):
        self._name = name.replace(CLAUSE_END, "")
        self._value = self._get_value(body)

    """ from string creates value of the fact"""
    @abstractmethod
    def _get_value(self, body):
        pass

    def name(self):
        return self._name[:]

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def fill_rest(self, set_values, keys, answerer):
        pass

    @abstractmethod
    def is_true(self, body, database):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

