from domains.repositories import IQuestionReader, IQuestionWriter
from domains.objects import Question as Aggregate
from .models import Question
from .serializers import QuestionSerializer


class QuestionReader(IQuestionReader):
    """
    DBアクセスのreadの実体
    """

    def read(self, id: str) -> Aggregate:
        """Aggregateを作成して返す
        """
        # Aggregete用のSerializerを定義して使っても良いかも
        aggregate_serializer = QuestionSerializer(Question.objects.get(id=id))

        tmp = QuestionSerializer(data=aggregate_serializer.data)
        tmp.is_valid()

        return Aggregate(**tmp.validated_data)


class QuestionWriter(IQuestionWriter):
    """
    DBアクセスのwriteの実体
    """

    def write(self, obj: Aggregate) -> Aggregate:
        tmp = Question(
            question_text=obj.question_text,
            pub_date=obj.pub_date,
        )
        tmp.save()

        return Aggregate(id=tmp.id,
                         question_text=obj.question_text,
                         pub_date=obj.pub_date)
