from typing import Union

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Profile


def user(request, username_or_id: Union[int, str]):
    try:
        profile = _get_profile(username_or_id)
        context = {'user_prof': {
            'username': profile.user.username,
            'image': profile.image,
            'gender': profile.get_gender_display(),
            'country': profile.get_country_display(),
            'city': profile.city,
            'date_of_birth': profile.date_of_birth,
            'audio_track': profile.audio_track
            },
            'title': profile
        }
        return render(request, 'myplace/profile.html', context)
    except Profile.DoesNotExist:
        messages.error(request, 'That user profile does not exist.')
        return redirect('home')


def _get_profile(username_or_id: Union[int, str]) -> Profile:
    if isinstance(username_or_id, int):
        return get_object_or_404(Profile, id=username_or_id)
    else:
        return get_object_or_404(Profile, user__username=username_or_id)
