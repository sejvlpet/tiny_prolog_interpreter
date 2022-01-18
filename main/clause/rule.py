from main.clause.clause import Clause
from main.constatnts import *
from main.question.is_question import Is_question
from main.question.custom_question import Custom_question
from copy import copy

"""
Rule is a clause consisting from predicate in head and predicates in body
for simplicity, only and in the body is implemented
"""
class Rule(Clause):

    def __init__(self, head, body):
        splitted_head = head.split(CLAUSE_START)

        self._params = splitted_head[1].split(CLAUSE_END)[0].split(ATOM_SEPARATOR)
        self._cutting = False # default value
        super().__init__(body, splitted_head[0])

    def __eq__(self, other):
        if isinstance(other, Rule):
            return self.compare_name_value(other._name, other._value, other._params, other._cutting)

        return False # unknown types do not equal

    def fill_rest(self, set_values, keys, answerer):
        """
        gets body with Nones on places need to be filled
        returns List with filled thing instead of Nones and Nones on prefilled places
        if body cannot be filled, returns None
        if situation cannot be decided, behavior is undefined
        """
        key_val = self._get_key_val(set_values)
        if not len(key_val):
            return
        cutting = False

        states, filling = [key_val], [{}]
        for q in self._value:  # here should be created questions with proper values
            for i in range(len(states)):
                state = states[i]
                # create and answer the question here
                q_object = self._create_question(q, state)
                answers, cutting = q_object.answer(answerer)
                if not answers: # ignore False answers
                    break
                if isinstance(answers, bool):
                    continue # do not fill anything for rules that were simply true
                # based on given answers
                states, filling = self._process_answer(answers, states, filling, i)
                if cutting:
                    break


        res = self._remap_filled_vars_to_asked(filling, keys)
        return res, cutting or self._cutting

    def _remap_filled_vars_to_asked(self, filling, keys):
        """ remaps inner param names to names asked from the object that was asking """
        value_of = {}
        for i in range(len(self._params)):
            if keys[i] is not None:
                value_of[keys[i]] = self._params[i]
        # exactly all asked keys have to be returns
        res = []
        for to_fill in filling:
            tmp_res = {}
            for key in value_of:
                val = value_of[key]
                if val in to_fill:
                    tmp_res[key] = to_fill[val]
            if len(tmp_res):
                res.append(tmp_res)
        return res

    def _process_answer(self, answers, states, filling, i):
        """ answer need to be stored to state and create new if needed """
        state, filler = states[i], filling[i]
        for answer_index in range(len(answers)):
            answer = answers[answer_index]
            new_i = i + answer_index
            if new_i >= len(states):
                states.append(copy(state))
                filling.append(copy(filler))
            states[new_i].update(answer)
            filling[new_i].update(answer)

            if new_i > 0 and states[new_i] == states[new_i - 1]:
                # remove duplicate states
                del states[new_i]
                del filling[new_i]


        return states, filling


    def is_true(self, body, answerer):
        """ method returns true if the rule with given parameters is true """
        for i in range(len(body)):
            # the rule is true if it at least once fills the requested value with the rest parameters given
            missed_value = body[i]
            set_values = [body[j] if j != i else None for j in range(len(body))]
            keys = ["X" if j == i else None for j in range(len(body))]
            answers, cutting = self.fill_rest(set_values, keys, answerer)

            for answer in answers:
                if answer["X"] == missed_value:
                    return True, cutting

        return False, False

    def size(self):
        return len(self._params)

    def compare_name_value(self, name, value, params, cutting):
        """ test method """
        if len(value) != len(self._value):
            return False

        for i in range(len(value)):
            if value[i] != self._value[i]:
                return False

        for i in range(len(params)):
            if params[i] != self._params[i]:
                return False

        return name == self._name and cutting == self._cutting

    def _get_key_val(self, body):
        """ assign values of params to proper param names """
        key_val = {}
        for i in range(len(self._params)):
            if body[i] is not None:
                # we're skipping None values, we're filling only the known ones
                name = self._params[i]
                val = body[i]
                key_val[name] = val
        return key_val

    def _get_value(self, body):
        """ read the input to proper shape """
        splitted = body.split(PREDICATE_SEPARATOR)
        if splitted[-1][-1] == CUT_SIGN:
            self._cutting = True
            splitted[-1] = splitted[-1][:-2]

        res = []
        for r in splitted:
            res.append(r.replace(CLAUSE_END, ""))

        return res

    def _create_question(self, q, key_val):
        """ fill parametrs to question and create an object that can answer it """
        q = q.replace(CLAUSE_END, "")

        # replace variables for values
        for key in key_val:
            q = q.replace(key, str(key_val[key]))

        return create_question(q)
