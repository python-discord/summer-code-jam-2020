from typing import Union
from datetime import date

from django.contrib import messages
from django.shortcuts import render

from users.models import Profile


def user(request, username_or_id: Union[int, str]):
    try:
        profile = _get_profile(username_or_id)
        context = {
            'profile': {
                'username': profile.user.username,
                'last_login': profile.user.last_login,
                'image': profile.image.url,
                'gender': profile.get_gender_display(),
                'country': profile.get_country_display(),
                'city': profile.city,
                'years_old': (date.today() - profile.date_of_birth).days // 365,
                'audio_track': profile.audio_track
            },
            'title': profile,
            'custom_css': profile.profile_css,
            'profile_comments': profile.comments.all()
        }
        return render(request, 'myplace/profile.html', context)
    except Profile.DoesNotExist:
        messages.error(request, 'That user profile does not exist.')
        return render(request, 'myplace/profile.html')


def _get_profile(username_or_id: Union[int, str]) -> Profile:
    if isinstance(username_or_id, int):
        return Profile.objects.get(id=username_or_id)
    else:
        return Profile.objects.get(user__username=username_or_id)
