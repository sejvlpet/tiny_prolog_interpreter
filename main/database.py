from main.clause.clause_reader import Clause_reader
from main.constatnts import *
from main.clause.fact import Fact
from main.clause.rule import Rule


"""
This file contents classes needed for proper function of our tiny-prolog database
"""


"""
Container for informations loaded from file, handles loading itself when constructor is called
"""
class Database:

    def __init__(self, file_path):
        self._setupped = False
        self._clauses = {}
        self._load_file(file_path)


    def clauses(self):
        return self._clauses

    def answer(self, name, body):
        """
        for a fact with given name and size of body returns either
        bool - if body contains only atoms
        List[dict] if body contains variables, each dict contains values need for
        the fact to be true
        """
        self._check_has_clause(name, len(body))
        clauses = self._clauses[name][len(body)]

        if self._only_atoms(body): # simple fact check
            for clause in clauses:
                is_true, cutting = clause.is_true(body)
                if is_true:
                    return is_true, cutting
            return False, False

        else:
            set_values = [x if is_atom(x) else None for x in body]
            keys = [x if not is_atom(x) else None for x in body]
            res = []
            for clause in clauses:

                # todo add checking for cut at this point, it should simply break out

                tmp_res = clause.fill_rest(set_values, keys)
                if tmp_res is not None:
                    res.append(tmp_res)
            return res



    def _check_has_clause(self, name, size):
        if name not in self._clauses or size not in self._clauses[name]:
            raise Exception(BAD_INPUT_MSG)

    def _only_atoms(self, body):
        for b in body:
            if not is_atom(b):
                return False
        return True

    """
    loads file and stores clauses, which should be in the file, throws expection in case of problems
    """
    def _load_file(self, file_path):
        with open(file_path, 'r') as file:
            data = file.read().replace('\n', '')

        lines = data.split(ITEM_END)

        for line in lines:
            line = line.strip().replace(" ", "").replace("\t", "")
            if not len(line):
                continue

            clause_reader = Clause_reader(line)
            clause = clause_reader.read()

            n, s = clause.name(), clause.size()
            # split clauses by name and count of their parameters
            if n not in self._clauses:
                self._clauses[n] = {}
            if s not in self._clauses[n]:
                self._clauses[n][s] = []

            self._clauses[n][s].append(clause)
