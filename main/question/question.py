from abc import ABC, abstractmethod

"""
Abstrat base class for other question

Generally, a question is and object which returns answers, those can be
    - true, if a the question is true due to some fact/rule from our database
    - false, if it is the answer to the question
    - suggestion - list of maps like strucutre, which returns possible values of variables for the
        question to be true
        
     
"""
class Question(ABC):


    @abstractmethod
    def answer(self):
        pass