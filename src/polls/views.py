from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Choice, Question
from .serializers \
    import ChoiceSerializer, QuestionSerializer, QuestionResponseSerializer

from domains.application_services import QuestionService
from .repositories import QuestionReader, QuestionWriter


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request, *args, **kwargs):
        # POSTで /api/polls/questions/ を実行した場合に実行されるmethod

        # request時のシリアライザ
        request_serializer = self.get_serializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        # QuestionServiceに処理委譲
        question_service = QuestionService(
            QuestionReader(),
            QuestionWriter(),
            request_serializer.validated_data
        )
        # responseとして返すデータ
        result = question_service.execute()

        # response時のシリアライザ
        response_serializer = QuestionResponseSerializer(data=result)
        response_serializer.is_valid(raise_exception=True)

        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
