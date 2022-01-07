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
PREDICATE_SEPARATOR = "),"
IS_SIGN = "is"
PLUS = "+"
MINUS = "-"
PRODUCT = "*"
ITEM_END = "." # wrong name, overriding aaaaa

def is_atom(x):
    return x.isdigit() or x[0].islower


