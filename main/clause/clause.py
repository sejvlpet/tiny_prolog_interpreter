from abc import ABC, abstractmethod

"""
Abstract parent to clauses

We shall differentiate between two types of clauses, rule and fact.
Fact is always true a can be either final (meaning it does cut (!)), or not. Only atoms in fact definition are allowed
Rule is true if it's body is true, body can consist from other clauses
"""
#  @abstractmethod will evaulate if someting true I guess or something like that
class Clause(ABC):


    def __init__(self, body):
        self._value = self._get_value(body)

    """ from string creates value of the fact"""
    @abstractmethod
    def _get_value(self, body):
        pass
