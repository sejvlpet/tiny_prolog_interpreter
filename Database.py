from Clause import *

"""
This file contents classes needed for proper function of our tiny-prolog database
"""


"""
Container for informations loaded from file, handles loading itself when constructor is called
"""
class Database:

    def __init__(self):
        self._setupped = False
        pass

    def __int__(self, file_path):
        self._clauses = []
        self._load_file(file_path)





    """
    loads file and stores clauses, which should be in the file, throws expection in case of problems
    """
    # fixme reading line by line is wrong, res should be splitted by "."
    def _load_file(self, file_path):
        file = open(file_path, "r")
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            clause_reader = Clause_reader(line)
            clause = clause_reader.read()
            self._clauses.append(clause)


