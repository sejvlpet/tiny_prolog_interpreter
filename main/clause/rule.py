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

    def __eq__(self, other):
        if isinstance(other, Rule):
            return self.compare_name_value(other._name, other._value, other._params, other._cutting)

        return False # unknown types do not equal

    def fill_rest(self, set_values, keys):
        """
        gets body with Nones on places need to be filled
        returns List with filled thing instead of Nones and Nones on prefilled places
        if body cannot be filled, returns None
        if situation cannot be decided, behavior is undefined
        """
        missing = {}

    def is_true(self, body):
        # map body to variable
        # as questions with properly mapped things
        key_val = {}
        for i in range(len(self._params)):
            name = self._params[i]
            val = body[i]
            key_val[name] = val
        for q in self._value: # here should be created questions with proper values
            # create and answer the question here
            q_object = self._create_question(q, key_val)

            if not q_object.answer(): # only and supported - all question must be true for a rule to be true
                return False, False # false never cuts

        return True, self._cutting



    def size(self):
        return len(self._params)

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

    """ from string creates value of the fact"""
    def _get_value(self, body): # fixme question shouldn't be created here, only the basis for them
        splitted = body.split(PREDICATE_SEPARATOR)
        if splitted[-1][-1] == CUT_SIGN:
            self._cutting = True
            splitted[-1] = splitted[-1][:-2]

        res = []
        for r in splitted:
            res.append(r.replace(CLAUSE_END, ""))

        return res

    def _create_question(self, q, key_val):

        q = q.replace(CLAUSE_END, "")
        if IS_SIGN in q:
            left, right = q.split(IS_SIGN)
            left_var = int(left) if left.isdigit() else left.strip()

            if PLUS in right or PRODUCT in right or MINUS in right:
                # get the right sin
                sign = PLUS if PLUS in right else None
                sign = MINUS if MINUS in right else sign
                sign = PRODUCT if PRODUCT in right else sign

                r1, r2 = right.split(sign)
                r1 = int(r1) if r1.isdigit() else r1
                r2 = int(r2) if r2.isdigit() else r2
                return Is_question(left_var, r1, r2, sign)
            else:
                return Is_question(left_var, q)

        elif CLAUSE_START in q:
            # handle clause by name and params
            return Custom_question(q)
