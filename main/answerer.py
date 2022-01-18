from main.clause.clause_reader import Clause_reader
from main.constatnts import *


class Answerer:
    """ Class handles answerin tu qestions """
    def __init__(self, database):
        self._database = database

    def answer(self, name, body):
        """
        for a fact with given name and size of body returns either
        bool - if body contains only atoms
        List[dict] if body contains variables, each dict contains values need for
        the fact to be true
        """
        self._check_has_clause(name, len(body))
        clauses = self._database.clauses()[name][len(body)]

        # note that for simplicity, negative number are not accepted
        for a in body:
            if isinstance(a, str) and len(a) > 1 and a[0] == "-" and a[1].isdigit():
                return False, False


        if self._only_atoms(body): # simple fact check
            for clause in clauses:
                is_true, cutting = clause.is_true(body, self)
                if is_true:
                    return True, cutting
            return False, False

        else:
            res = []
            set_values = [x if is_atom(x) else None for x in body]
            keys = [x if not is_atom(x) else None for x in body]
            for clause in clauses:

                tmp_res = clause.fill_rest(set_values, keys, self)
                # print(tmp_res)
                if tmp_res is not None:
                    t, cutting = tmp_res
                    res.append(t)
                    if cutting:
                        break

            # todo return all possibles fillers
            return res[0], cutting



    def _check_has_clause(self, name, size):
        if name not in self._database.clauses() or size not in self._database.clauses()[name]:
            raise Exception(BAD_INPUT_MSG)

    def _only_atoms(self, body):
        for b in body:
            if not is_atom(b):
                return False
        return True