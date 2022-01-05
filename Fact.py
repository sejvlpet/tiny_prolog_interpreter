from Constatnts import *
from Clause import Clause

"""
Fact shall have a name and a value, where value is a list of atoms
"""
class Fact(Clause):

    def __init__(self, fact, cutting):
        splitted = fact.split(FACT_START)

        self._name = splitted[0]
        self._value = self._get_value(splitted[1].split(FACT_END)[0])
        self._cutting = cutting

    """ from string creates value of the fact"""
    def _get_value(self, fact_body):
        splitted = fact_body.strip().split(ATOM_SEPARATOR)

        for i in range(len(splitted)):
            splitted[i] = splitted[i].strip()
            a = splitted[i]

            # taking atoms only - ints, or string starting by lowercase
            if a.isdigit():
                splitted[i] = int(splitted[i])

            elif a[0].isupper():
                raise Exception(BAD_INPUT_MSG)

        return splitted



    # --------- test methods --------
    def compare_name_value(self, name, value, cutting):
        if len(value) != len(self._value):
            return False

        for i in range(len(value)):
            if value[i] != self._value[i]:
                return False

        return name == self._name and cutting == self._cutting