from main.clause.clause_reader import Clause_reader
from main.constatnts import *

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

    def contains_fact(self, name, body):
        """
        for a fact with given name and size of body returns either
        bool - if body contains only atoms
        List[dict] if body contains variables, each dict contains values need for
        the fact to be true
        """
        self._check_has_clause(name, len(body))
        if self._only_atoms(body):
            return body in self._clauses[name][len(body)]

        else:
            # todo return list of dicts with needed values to be true
            pass




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
            line = line.strip().replace(" ", "")
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

