from constatnts import *
from database import Database
"""
    Runs program

    Program is an interactive application based on Prolog, there are two possible commands
        - consult(file_path) - loads new database of facts and rules from file_path, syntax is polog-like
            and should be obvious from examples, also described in readme
        - ?- question, also prolog-like syntax. The Question is either answered by bool, or possible atom
            instead of variable in the question is suggested. If there are more possibilities for fillup, all will be displayed.
"""


def bad_input():
    print(BAD_INPUT_MSG)

def main():
    database = None

    while True:
        com = input().strip().replace(" ", "")
        consult_len = len(CONSULT)
        q_mark_len = len(Q_MARK)

        if len(com) >= consult_len and com[: consult_len + 1] == CONSULT + "(" and com[-2:] == ").":
            # this branch shall recreate DB

            file_path = com[consult_len: ]
            database = Database(file_path)

        elif len(com) >= q_mark_len and com[: 2] == Q_MARK:
            # load & answer the question
            question_str = com[q_mark_len: ]
            question = create_question(question_str)
            print(question_str)
            print(question.answer()[0])

        else:
            bad_input()




if __name__ == "__main__":
    main()