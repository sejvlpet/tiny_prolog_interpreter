from main.constatnts import *
from main.clause.clause import Clause
from typing import List

"""
Fact shall have a name and a value, where value is a list of atoms
"""


class Fact(Clause):

    def __init__(self, fact, cutting):
        splitted = fact.split(CLAUSE_START)
        body = splitted[1].split(CLAUSE_END)[0]
        super().__init__(body, splitted[0])

        self._cutting = cutting

    def __eq__(self, other):
        if isinstance(other, Fact):
            return self.compare_name_value(other._name, other._value, other._cutting)

        if isinstance(other, List):
            return self._value == other

        return False  # unknown types do not equal

    def fill_rest(self, set_values, keys, _=None):
        """
        gets body with Nones on places need to be filled
        returns List with filled thing instead of Nones and Nones on prefilled places
        if body cannot be filled, returns None
        """
        missing = {}
        for i in range(len(set_values)):
            val, key, self_val = set_values[i], keys[i], self._value[i]
            if val is not None and val != self_val:  # check if this fact is usable
                return None

            if val is None:
                missing[key] = self_val

        return missing

    def is_true(self, body, _=None):
        """ fact is true if all body values are the same as self._value"""
        return self._value == body, self._cutting

    def size(self):
        return len(self._value)

    """ test method """

    def compare_name_value(self, name, value, cutting):
        if len(value) != len(self._value):
            return False

        for i in range(len(value)):
            if value[i] != self._value[i]:
                return False

        return name == self._name and cutting == self._cutting

    """ from string creates value of the fact"""

    def _get_value(self, body):
        splitted = body.strip().split(ATOM_SEPARATOR)

        for i in range(len(splitted)):
            splitted[i] = splitted[i].strip()
            a = splitted[i]

            # taking atoms only - ints, or string starting by lowercase
            if a.isdigit():
                splitted[i] = int(splitted[i])

            elif a[0].isupper():
                raise Exception(BAD_INPUT_MSG)

        return splitted
