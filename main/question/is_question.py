from main.question.question import Question
from main.constatnts import *


"""
handles question of is type
"""
class Is_question(Question):

    def __init__(self, left_var, r1, r2=None, sign=None):
        self._left_var = left_var
        self._r1 = r1
        self._r2 = r2
        self._sign = sign

    def __eq__(self, other):
        return self._left_var == other._left_var and self._r1 == other._r1 \
               and self._r2 == other._r2 and self._sign == other._sign

    """
    return either true, or value for left var
    """
    def answer(self):
        if self._left_var is None:
            return self._handle_right_side()

        else:
            return self._left_var == self._handle_right_side()



    def _handle_right_side(self):
        if self._r2 is None:
            return self._r1

        if self._sign == PLUS:
            return self._r1 + self._r2
        if self._sign == PRODUCT:
            return self._r1 * self._r2

        else:
            raise Exception(BAD_INPUT_MSG)