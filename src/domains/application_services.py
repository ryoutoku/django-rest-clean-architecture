from .repositories import IQuestionReader, IQuestionWriter
from .objects import Question


class QuestionService:

    def __init__(self,
                 reader: IQuestionReader,
                 writer: IQuestionWriter,
                 data: dict):
        self._reader = reader
        self._writer = writer
        self._data = data

    def execute(self) -> dict:
        """
        execute 業務ロジックをここで実行
        """
        # 1. 場合に応じてquestion(Aggregate)を生成するかDBから読み込む
        # 読み込む場合
        # question = self._reader.read(self._data["id"])

        question = Question(
            question_text=self._data["question_text"],
            pub_date=self._data["pub_date"])

        # Aggregateを使って業務ロジックを実行

        # 保存
        result = self._writer.write(question)

        # returnはI/Fを意識したdictを返す
        return {
            "id": result.id,
            "pub_date": str(result.pub_date),
            "question_text": result.question_text
        }
