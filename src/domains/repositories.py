from abc import ABC, abstractmethod

from .objects import Question


class IQuestionReader(ABC):
    """
    IQuestionReader DB readのinterface
    """

    @abstractmethod
    def read(self, id: str) -> Question:
        # DBからidに合致するデータ取得し、
        # Aggregate(Question)を生成して返すロジックを実装する
        raise NotImplementedError()


class IQuestionWriter(ABC):
    """
    IQuestionWriter DB writeのinterface
    """

    @abstractmethod
    def write(self, obj: Question):
        # Aggregate(Question)を受け、DBに保存するロジックを実装する
        raise NotImplementedError()
