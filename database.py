from clause.clause_reader import Clause_reader
from constatnts import *
from clause.fact import Fact
from clause.rule import Rule
from answerer import Answerer

class Database:
    """
    Container for informations loaded from file, handles loading itself when constructor is called
    """
    def __init__(self, file_path):
        self._setupped = False
        self._clauses = {}
        self._load_file(file_path)
        self._answerer = Answerer(self)


    def clauses(self):
        return self._clauses

    def answer(self, name, body):
        return self._answerer.answer(name, body)

    def _load_file(self, file_path):
        """
        loads file and stores clauses, which should be in the file, throws expection in case of problems
        """
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

        self._sort_clauses()

    def _sort_clauses(self):
        """ place facts firt, so they're asked first """
        for name in self._clauses:
            for count in self._clauses[name]:
                r = []
                for tmp in self._clauses[name][count]:
                    if isinstance(tmp, Fact):
                        r.append(tmp)
                for tmp in self._clauses[name][count]:
                    if isinstance(tmp, Rule):
                        r.append(tmp)
                self._clauses[name][count] = r