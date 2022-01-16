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

        self._facts = {}
        self._rules = {}

        self._load_file(file_path)


    def clauses(self):
        return self._clauses

    # todo this method may need a refactor
    def contains_fact(self, name, body):
        """
        for a fact with given name and size of body returns either
        bool - if body contains only atoms
        List[dict] if body contains variables, each dict contains values need for
        the fact to be true
        """
        self._check_has_clause(name, len(body), self._facts)
        facts = self._facts[name][len(body)]
        if self._only_atoms(body):
            return body in facts

        else:
            set_values = [x if is_atom(x) else None for x in body]
            keys = [x if not is_atom(x) else None for x in body]
            res = []
            for fact in facts:
                tmp_res = fact.fill_rest(set_values, keys)
                if tmp_res is not None:
                    res.append(tmp_res)
            return res



    def _check_has_clause(self, name, size, clauses):
        if name not in clauses or size not in clauses[name]:
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

        self._split_facts_and_rules()

    def _split_facts_and_rules(self):
        # over time it started to be handy to have facts and rules splited, this method give a space for refactor
        for name in self._clauses:
            for argc in self._clauses[name]:
                for tmp in self._clauses[name][argc]:

                    if isinstance(tmp, Fact):
                        if name not in self._facts:
                            self._facts[name] = {}
                        if argc not in self._facts[name]:
                            self._facts[name][argc] = []
                        self._facts[name][argc].append(tmp)

                    elif isinstance(tmp, Rule):
                        if name not in self._rules:
                            self._rules[name] = {}
                        if argc not in self._rules[name]:
                            self._rules[name][argc] = []
                        self._rules[name][argc].append(tmp)
