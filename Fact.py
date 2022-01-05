from Constatnts import *
from Clause import Clause

"""
Fact shall have a name and a value, where value is a list of atoms
"""
class Fact(Clause):

    def __init__(self, fact, cutting):
        self._check_fact(fact)
        splitted = fact.split(FACT_START)

        self._name = splitted[0]
        self._value = self._get_value(splitted[1][len(FACT_START): -len(FACT_END)])
        self._cutting = cutting


    """ from string creates value of the fact"""
    def _get_value(self, fact_body):
        splitted = fact_body.strip().split(ATOM_SEPARATOR)

        for i in range(splitted):
            a = splitted[i]

            # taking atoms only - ints, or string starting by lowercase
            if a.is_integer():
                splitted[i] = int(splitted[i])
            elif a[0].isupper():
                raise Exception(BAD_INPUT_MSG)

        return splitted

    """ checks if fact has a proper shape"""
    def _check_fact(self, fact):
        # some basic check for proper fact, may not be completely bulletproof
        if len(fact) < MIN_FACT_LEN or FACT_START not in fact or fact[-len(FACT_END): ] != FACT_END:
            raise Exception(BAD_INPUT_MSG)