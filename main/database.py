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
        self._clauses = []
        self._clauses = {}
        self._load_file(file_path)


    def clauses(self):
        return self._clauses



    """
    loads file and stores clauses, which should be in the file, throws expection in case of problems
    """
    # fixme reading line by line is wrong, res should be splitted by "."
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

