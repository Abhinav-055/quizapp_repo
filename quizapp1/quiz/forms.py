from django import forms
from .models import Quiz, Question, Option
from django.forms import inlineformset_factory
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'is_correct']
OptionFormSet = inlineformset_factory(Question, Option, form=OptionForm, extra=0)  
QuestionFormSet = inlineformset_factory(Quiz, Question, fields=['text'], extra=1)