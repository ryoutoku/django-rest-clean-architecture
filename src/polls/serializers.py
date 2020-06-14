from datetime import datetime

from rest_framework import serializers

from .models import Choice, Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question_text = serializers.CharField(max_length=10)
    pub_date = serializers.DateTimeField()


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ("choice_text",
                  "votes")

    question = QuestionSerializer

    def validate_choice_text(self, choice_text):
        # ここにchoice_textのvalidationロジックを書く
        return choice_text
