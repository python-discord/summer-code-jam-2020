from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ForumUserChangeForm


@login_required
def message(request, m_id):
    if request.method == "DELETE":
        pass  # @TODO: Handle message deletion

    elif request.method == "PATCH":
        pass  # @TODO: Handle message edit


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = ForumUserChangeForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
        return redirect('profile')
    else:
        u_form = ForumUserChangeForm(instance=request.user)

    context = {"u_form": u_form}
    return render(request, 'user/profile.html', context)
