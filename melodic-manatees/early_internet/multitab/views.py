from django.shortcuts import render, redirect
from .models import MultiTab
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
'''Views for the MultiTab app'''


@login_required(login_url='login')
def multitab_home(request):
    # get all MultiTab objects for the current user
    multitabs = MultiTab.objects.filter(multitab_owner=request.user.profile)
    if multitabs:
        if len(multitabs) == 1:
            title_1 = multitabs[0].title
            site_1_1 = multitabs[0].tab_one
            site_1_2 = multitabs[0].tab_two
            site_1_3 = multitabs[0].tab_three
            title_2 = 'Multitab'
            site_2_1 = multitabs[1].tab_one
            site_2_2 = multitabs[1].tab_two
            site_2_3 = multitabs[1].tab_three
        elif len(multitabs) == 2:
            title_1 = multitabs[0].title
            site_1_1 = multitabs[0].tab_one
            site_1_2 = multitabs[0].tab_two
            site_1_3 = multitabs[0].tab_three
            title_2 = multitabs[1].title
            site_2_1 = multitabs[1].tab_one
            site_2_2 = multitabs[1].tab_two
            site_2_3 = multitabs[1].tab_three
    else:
        title_1 = 'Multitab'
        site_1_1 = ''
        site_1_2 = ''
        site_1_3 = ''
        title_2 = 'Multitab'
        site_2_1 = ''
        site_2_2 = ''
        site_2_3 = ''
    number_of_multitabs = list('_' for x in range(len(multitabs)))
    print(number_of_multitabs)
    return render(
        request,
        'multitab/multitab.html',
        {
            'title_1': title_1,
            'site_1_1': site_1_1,
            'site_1_2': site_1_2,
            'site_1_3': site_1_3,
            'title_2': title_2,
            'site_2_1': site_2_1,
            'site_2_2': site_2_2,
            'site_2_3': site_2_3,
            'number_of_multitabs': number_of_multitabs
        }
    )


@login_required(login_url='login')
def add_multitab(request):
    # create a formset with the base form to a max of 2 forms.
    multitab_form = modelformset_factory(
        MultiTab,
        fields=(
            'title',
            'tab_one',
            'tab_two',
            'tab_three'
            ),
        extra=2,
        max_num=2,
        )
    if request.method == 'POST':
        formset = multitab_form(
            request.POST,
            queryset=MultiTab.objects.filter(
                multitab_owner=request.user.profile)
        )
        if formset.is_valid():
            # if valid, for every formset, save that instance.
            instances = formset.save(commit=False)
            for instance in instances:
                instance.multitab_owner = request.user.profile
                instance.save()
            return redirect('multitab-home')
    else:
        formset = multitab_form(
            queryset=MultiTab.objects.filter(
                multitab_owner=request.user.profile
            )
        )
    return render(
        request,
        'multitab/edit_multitab.html',
        {
            'formset': formset
        }
        )
