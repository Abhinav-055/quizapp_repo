from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Quiz, Question, Option
from .forms import QuizForm, QuestionForm, OptionFormSet
from django.shortcuts import render, redirect
from .forms import QuizForm, QuestionFormSet

def create_quiz(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        question_formset = QuestionFormSet(request.POST, prefix='questions', queryset=Question.objects.none())

        if quiz_form.is_valid() and question_formset.is_valid():
            quiz = quiz_form.save()
            questions = question_formset.save(commit=False)
            print(question_formset)
            for question in questions:
                question.quiz = quiz
                question.save()

                # Process options for each question
                option_formset = OptionFormSet(request.POST, prefix=f'options-{question.id}', instance=question)
                print(option_formset)
                if option_formset.is_valid():
                    options = option_formset.save(commit=False)
                    
                    for option in options:
                        option.question = question
                        option.save()
                        print("Options saved successfully for question:", question.text)

            print("End of the loop")

            return render(request, 'quiz/quiz_list.html') 
        else:
            print("Form validation failed.")
            print("Quiz Form Errors:", quiz_form.errors)
            print("Question Formset Errors:", question_formset.errors)
    else:
        quiz_form = QuizForm()
        question_formset = QuestionFormSet(prefix='questions')

    return render(request, 'quiz/create_quiz.html', {'quiz_form': quiz_form, 'question_formset': question_formset})
def quiz_list(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quiz_list': quiz_list})
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    context = {'quiz': quiz, 'questions': questions}
    return render(request, 'quiz/quiz_detail.html', context)

def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle saving and scoring logic here
            return HttpResponseRedirect(reverse('quiz:quiz_detail', args=(quiz_id,)))
    else:
        form = QuizForm()

    return render(request, 'quiz/quiz_form.html', {'form': form})
def home(request):
    return render(request,'quiz/home.html')