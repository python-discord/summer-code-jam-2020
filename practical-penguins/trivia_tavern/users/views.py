from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from trivia_builder.models import TriviaQuiz
from trivia_runner.models import ActiveTriviaQuiz
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in as {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    user_quizzes = TriviaQuiz.objects.filter(author=request.user)
    current_hosted_session = ActiveTriviaQuiz.objects.filter(session_master=request.user)
    return render(request, 'users/profile.html', {'user': request.user,
                                                  'user_quizzes': user_quizzes,
                                                  'user_active_session': current_hosted_session})


def profile_user(request, username):
    user = User.objects.get(username=username)
    user_quizzes = TriviaQuiz.objects.filter(author=user)
    current_hosted_session = ActiveTriviaQuiz.objects.filter(session_master=request.user)
    return render(request, 'users/profile.html', {'user': request.user,
                                                  'user_quizzes': user_quizzes,
                                                  'user_active_session': current_hosted_session})


@login_required
def results(request):
    return render(request, 'users/results.html')
