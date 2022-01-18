from abc import ABC, abstractmethod


class Question(ABC):
    """
    Abstrat base class for other question

    Generally, a question is an object which returns answers, those can be
        - true, if a the question is true due to some fact/rule from our database
        - false, if it is the answer to the question
        - suggestion - list of maps, which returns possible values of variables for the
            question to be true


    """
    @abstractmethod
    def answer(self, answerer):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass
