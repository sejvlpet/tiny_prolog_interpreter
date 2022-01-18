"""
Constants and helper functions used over the application
"""
CONSULT = "consult"
Q_MARK  = "?-"
BAD_INPUT_MSG = "Bad input, try again"
IMPL_SIGN = ":-"
CUT_SIGN = "!"
CLAUSE_START = "("
CLAUSE_END = ")"
MIN_FACT_LEN = len(CLAUSE_START) + len(CLAUSE_END) + 1
ATOM_SEPARATOR = ","
PREDICATE_SEPARATOR = "&"
IS_SIGN = "is"
PLUS = "+"
MINUS = "-"
PRODUCT = "*"
ITEM_END = "."


def is_atom(x):
    return isinstance(x, int) or x[0].islower() or x.isdigit()


def create_question(q):
    """ from question string creates a question object """
    from question.is_question import Is_question
    from question.custom_question import Custom_question
    if IS_SIGN in q:
        left, right = q.split(IS_SIGN)
        left_var = int(left) if left.isdigit() else left.strip()

        if PLUS in right or PRODUCT in right or MINUS in right:
            # get the right sin
            sign = PLUS if PLUS in right else None
            sign = MINUS if MINUS in right else sign
            sign = PRODUCT if PRODUCT in right else sign

            r1, r2 = right.split(sign)
            r2 = r2.split(ITEM_END)[0] # decline the end dot in case of last item in a question/line/rule
            r1 = int(r1) if r1.isdigit() else r1
            r2 = int(r2) if r2.isdigit() else r2
            return Is_question(left_var, r1, r2, sign)
        else:
            return Is_question(left_var, q)

    elif CLAUSE_START in q:
        # handle clause by name and params
        return Custom_question(q)