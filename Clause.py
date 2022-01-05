from abc import ABC, abstractmethod
from Constatnts import *
from Fact import Fact

"""
File contents code needed for clause funcionality
"""

"""
Abstract parent to clauses

We shall differentiate between two types of clauses, rule and fact.
Fact is always true a can be either final (meaning it does cut (!)), or not. Only atoms in fact definition are allowed
Rule is true if it's body is true, body can consist from other clauses
"""
#  @abstractmethod
class Clause:
    pass


"""
Handles translation from line given to constructor to proper clause, either fact or rule
"""
class Clause_reader:


    def __init__(self, line):
        self._line = line

    """ from self._line reads and return the clause """
    def read(self):

        if self._reading_fact():
            cutting = False
            if IMPL_SIGN in self._line:
                cutting = True # look at _reading_fact, cutting sign had to be present in this case

            return Fact(self._line.split(IMPL_SIGN)[0].trim(), cutting)

        else:
            # todo read a rule
            pass


    def _reading_fact(self):

        # checks for simple fact or fact with a cut
        if IMPL_SIGN not in self._line or self._line.split(IMPL_SIGN)[1].trim() != CUT_SIGN:
            return True
        else:
            return False
