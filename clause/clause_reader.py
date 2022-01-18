from constatnts import *
from clause.fact import Fact
from clause.rule import Rule

class Clause_reader:
    """
    Handles translation from line given to constructor to proper clause, either fact or rule
    """

    def __init__(self, line):
        self._line = line

    def read(self):
        """ from self._line reads and return the clause """

        if self._reading_fact():
            cutting = False
            if IMPL_SIGN in self._line:
                cutting = True # look at _reading_fact, cutting sign had to be present in this case

            return Fact(self._line.split(IMPL_SIGN)[0].strip(), cutting)

        else:
            # otherwise rule is read
            splitted = self._line.split(IMPL_SIGN)
            name = splitted[0]
            body = splitted[1]
            return Rule(name, body)




    def _reading_fact(self):

        # checks for simple fact or fact with a cut
        if IMPL_SIGN not in self._line or self._line.split(IMPL_SIGN)[1].strip() == CUT_SIGN:
            return True
        else:
            return False
