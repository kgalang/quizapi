from rest_framework import viewsets
from quizapi.serializers import QuizSerializer
from quizzes.models import Quiz

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
