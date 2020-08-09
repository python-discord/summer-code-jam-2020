from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from trivia_builder.forms import TriviaQuizForm, TriviaQuestionForm
from trivia_builder.models import TriviaQuiz, TriviaQuestion
from trivia_runner.models import ActiveTriviaQuiz


class TriviaQuizListView(ListView):
    model = TriviaQuiz
    template_name = 'trivia_builder/quiz_list.html'
    context_object_name = 'quizzes'
    ordering = ['-date_posted']
    paginate_by = 10


class PassRequestToFormViewMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UserTriviaQuizListView(ListView):
    model = TriviaQuiz
    template_name = 'trivia_builder/user_quizzes.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'TriviaQuiz'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return TriviaQuiz.objects.filter(author=user).order_by('-date_posted')


class TriviaQuizDetailView(DetailView):
    model = TriviaQuiz
    context_object_name = 'quiz'
    template_name = 'trivia_builder/triviaquiz_detail.html'

    def post(self, request, *args, **kwargs):
        active_trivia_quiz = ActiveTriviaQuiz.objects.create(trivia_quiz=self.get_object(),
                                                             session_master=request.user)
        active_trivia_quiz.save()
        return HttpResponseRedirect(reverse('activequiz', kwargs={'pk': active_trivia_quiz.pk}))


class TriviaQuizCreateView(PassRequestToFormViewMixin, LoginRequiredMixin, CreateView):
    model = TriviaQuiz
    fields = ['name']
    template_name = 'trivia_builder/triviaquiz_form.html'

    def post(self, request, *args, **kwargs):
        quiz_form = TriviaQuizForm(request.POST)
        TriviaQuestionFormSet = modelformset_factory(TriviaQuestion, form=TriviaQuestionForm)
        question_formset = TriviaQuestionFormSet(request.POST)
        new_questions = []
        if quiz_form.is_valid() and question_formset.is_valid():
            quiz_form.instance.author = self.request.user
            quiz = quiz_form.save()
            for i, question_form in enumerate(question_formset.forms, start=1):
                question_form.instance.quiz = quiz
                question_form.instance.question_index = i
                question = question_form.save()
                new_questions.append(question)
            question_formset.save()

            try:
                with transaction.atomic():
                    TriviaQuestion.objects.bulk_create(new_questions)
                    quiz.save()

                    # And notify our users that it worked
                    messages.success(request, 'You have created your quiz.')
                    return HttpResponseRedirect(reverse('quiz-list'))

            except IntegrityError:  # If the transaction failed
                messages.error(request, 'There was an error saving your profile.')
                return redirect(reverse('quiz-list'))
        return render(request, self.template_name, {'quiz_form': quiz_form, 'question_formset': question_formset})

    def get(self, request, *args, **kwargs):
        quiz_form = TriviaQuizForm()
        TriviaQuestionFormSet = modelformset_factory(TriviaQuestion, form=TriviaQuestionForm, extra=1)
        question_formset = TriviaQuestionFormSet(queryset=TriviaQuestion.objects.none())
        return render(request, self.template_name, {'quiz_form': quiz_form, 'question_formset': question_formset})


class TriviaQuizUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TriviaQuiz
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        trivia_quiz = self.get_object()
        if self.request.user == trivia_quiz.author:
            return True
        return False


class TriviaQuizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TriviaQuiz
    success_url = '/quiz'

    def test_func(self):
        trivia_quiz = self.get_object()
        if self.request.user == trivia_quiz.author:
            return True
        return False
