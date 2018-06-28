from quizzes.models import Quiz, Question, Choice
from rest_framework import serializers

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('__all__')

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question', 'choices')

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ('id', 'title', 'questions')