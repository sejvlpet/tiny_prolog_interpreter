from constatnts import *
from database import Database
from question.is_question import Is_question
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
        print("Enter your command")
        com = input().strip().replace(" ", "")
        consult_len = len(CONSULT)
        q_mark_len = len(Q_MARK)

        if len(com) >= consult_len and com[: consult_len + 1] == CONSULT + "(" and com[-2:] == ").":
            # this branch shall recreate DB

            file_path = com[consult_len: ]
            database = Database(file_path[1: -2])
            print("sucess")

        elif len(com) >= q_mark_len and com[: 2] == Q_MARK:
            # load & answer the question
            question_str = com[q_mark_len: ]
            question = create_question(question_str)
            if isinstance(question, Is_question):
                print(question.answer()[0])
            else:
                if database is None:
                    bad_input()
                else:
                    print(database.answer(question.name(), question.body())[0])

        else:
            bad_input()




if __name__ == "__main__":
    main()