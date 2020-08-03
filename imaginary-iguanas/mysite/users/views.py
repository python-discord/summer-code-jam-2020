from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required

from .forms import MySiteUserCreationForm, MySiteUserProfileSettingsForm


class SignUpView(CreateView):
    form_class = MySiteUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def user(request, user_id):
    # user_obj = User.objects.get(pk=user_id)
    # return render(request, 'user/user.html', {'user': user_obj})
    return render(request, 'users/user.html')


# @login_required
def user_settings(request):

    '''
        if request.method == 'POST':
        update_form = MySiteUserProfileSettingsForm(request.POST, request.FILES, instance=request.user)
        if update_form.isvalid():
            update_form.save()
            messages.success(request, f'Your profile has been updated successfully :)')
            return redirect('profile')
    else:
        update_form = MySiteUserProfileSettingsForm(instance=request.user)
    '''
    update_form = MySiteUserProfileSettingsForm()

    context = {
        'update_form': update_form
    }
    return render(request, 'settings.html', context)
