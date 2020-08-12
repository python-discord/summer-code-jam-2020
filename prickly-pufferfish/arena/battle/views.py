from django.views.generic import DetailView, RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Battle, Challenger

import os
import random


class RandomQuestion():
    def question(self):
        path = "python_questions"
        append_string = ''
        list_of_strings = []
        names = os.listdir(path)
        # removes hidden files, just in case.
        names = [f for f in names if not f.startswith('.')]
        list_of_paths = []
        for root, dirs, files in os.walk(path):
            for f in files:
                x = os.path.join(root, f)
                list_of_paths.append(x)

        question = random.choice(list_of_paths)
        open_question = open(question, 'r')
        display_question = open_question.read()
        display_question = display_question[3:-4]

        for i in display_question:
            if i != '\n':
                append_string += i
            if i == '/':
                list_of_strings.append(append_string[0:-1])
                append_string = ""
        return list_of_strings

    def name(self):
        path = "python_questions"
        names = os.listdir(path)
        # removes hidden files, just in case.
        names = [f for f in names if not f.startswith('.')]
        name = random.choice(names)
        return name


my_class = RandomQuestion()


class BattleView(DetailView):
    model = Battle
    template_name = 'battle/battle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['battle_id'] = self.get_object().pk
        return context


class PreBattleView(LoginRequiredMixin, SingleObjectMixin, RedirectView):
    model = Battle
    pattern_name = 'battle'

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if request.user.profile.in_battle():
            self.current_pk = request.user.profile.current_battle().pk
        elif queryset.filter(state=Battle.WAITING).count() > 0:
            battle = queryset.filter(state=Battle.WAITING).order_by('-pk')[0]
            if battle.challengers.count() == 0:
                battle.challengers.add(request.user)
                battle.save()
                self.current_pk = battle.pk
            else:
                color = Challenger.BLUE
                if battle.challenger_set.get().color == Challenger.BLUE:
                    color = Challenger.RED
                battle.challengers.add(request.user, through_defaults={'color': color})
                battle.state = Battle.READY
                battle.save()
                self.current_pk = battle.pk
        else:
            battle = Battle.objects.create()
            battle.challengers.add(request.user)
            battle.save()
            self.current_pk = battle.pk
        if request.user.battles.exclude(state=Battle.ARCHIVED).count() > 2:
            print('DEBUG LN 89 battle/views.py')
            request.user.challenges.exclude(
                battle__state=Battle.ARCHIVED, battle__pk=self.current_pk
            ).delete()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(self.current_pk, *args, **kwargs)
