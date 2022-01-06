from constatnts import *
"""
    Runs program

    Program is an interactive application based on Prolog, there are two possible commands
        - consult(file_path) - loads new database of facts and rules from file_path, syntax is polog-like
            and should be obvious from examples
        - ?- question, also prolog-like syntax. The Question is either answered by bool, or possible atom
            instead of variable in the question is suggested. If there are more possibilities for suitable atom,
            enter ; to see them.
"""

# todo needs to be testable, co run in two modes, one from input, second from tests

def bad_input():
    print(BAD_INPUT_MSG)

def main():
    # database = Database() todo

    while True:
        com = input().strip()
        consult_len = len(CONSULT)
        q_mark_len = len(Q_MARK)

        if len(com) >= consult_len and com[: consult_len + 1] == CONSULT + "(" and com[-1] == ")":
            # this branch shall recreate DB

            file_path = com[consult_len + 1 : -1]
            # database = Database(file_path) # todo, also consider some try/catch for loading

        elif len(com) >= q_mark_len and com[: 2] == Q_MARK:
            # load & answer the question
            question_str = com[q_mark_len: ]
            # question = Question(question_str) # todo
            # question.answer()

        else:
            bad_input()




if __name__ == "__main__":
    main()