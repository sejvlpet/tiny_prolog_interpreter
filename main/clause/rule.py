from main.clause.clause import Clause
from main.constatnts import *
from main.question.is_question import Is_question
from main.question.custom_question import Custom_question


"""
Rule is a clause consisting from predicate in head and predicates in body
for simplicity, only and in the body is implemented
"""
class Rule(Clause):

    def __init__(self, head, body):
        splitted_head = head.split(CLAUSE_START)

        # fixme this should rather be new object, predicate or something like that
        self._params = splitted_head[1].split(CLAUSE_END)[0].split(ATOM_SEPARATOR)
        self._cutting = False # default value
        super().__init__(body, splitted_head[0])


    """ from string creates value of the fact"""
    def _get_value(self, body):
        splitted = body.split(PREDICATE_SEPARATOR)
        if splitted[-1][-1] == CUT_SIGN:
            self._cutting = True
            splitted[-1] = splitted[-1][:-2]
        body = []

        for r in splitted:
            r = r.replace(" ", "")
            if IS_SIGN in r:
                left, right = r.split(IS_SIGN)
                left_var = int(left) if left.isdigit() else None

                if PLUS in right or PRODUCT in right or MINUS in right:
                    # get the right sin
                    sign = PLUS if PLUS in right else None
                    sign = MINUS if MINUS in right else sign
                    sign = PRODUCT if PRODUCT in right else sign

                    r1, r2 = right.split(sign)
                    r1 = int(r1) if r1.isdigit() else r1
                    r2 = int(r2) if r2.isdigit() else r2
                    body.append(Is_question(left_var, r1, r2, sign))
                else:
                    body.append(Is_question(left_var, r1))

            elif CLAUSE_START in r:
                # handle clause by name and params
                body.append(Custom_question(r))

        return body

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