from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Choice

# Register your models here.

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 4

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('Question', {'fields': ['question']}),
#     ]
#     inlines = [ChoiceInline]

# admin.site.register(Question, QuestionAdmin)

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [ChoiceInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)