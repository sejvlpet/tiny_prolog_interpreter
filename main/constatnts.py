"""
Constants used over the application
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
ITEM_END = "." # wrong name, overriding aaaaa


def is_atom(x):
    # or (len(x) > 1 and x[0] == "-" and x[1].isdigit()
    return isinstance(x, int) or x[0].islower() or x.isdigit()


