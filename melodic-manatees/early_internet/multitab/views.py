from django.shortcuts import render, redirect
from .models import MultiTab
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required


def multitab_home(request):
    multitabs = MultiTab.objects.filter()
    return render(request, 'multitab/multitab.html')


@login_required(login_url='login')
def add_multitab(request):
    multitab_form = modelformset_factory(
        MultiTab,
        fields=(
            'title',
            'tab_one',
            'tab_two',
            'tab_three'
            ),
        extra=4,
        max_num=4
        )
    if request.method == 'POST':
        formset = multitab_form(request.POST, queryset=MultiTab.objects.filter(multitab_owner=request.user))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.multitab_owner = request.user
                instance.save()
            return redirect('multitab-home')
    else:
        formset = multitab_form()
    return render(
        request,
        'multitab/edit_multitab.html',
        {
            'formset': formset
        }
        )
