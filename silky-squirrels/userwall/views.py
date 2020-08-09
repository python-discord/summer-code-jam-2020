from django.shortcuts import render, redirect
from userwall.forms import WallCreationForm
from django.contrib import messages
from users.models import Profile, User, ChatRoomVisit


# Create your views here.

# test website (blank)
def test(request, wall_name):
    print("default", request)
    return render(request, "userwall/potato.html", {"title": "test"})


def wall(request, profile_name):
    try:
        user = User.objects.get(username=profile_name)
        profile = Profile.objects.get(user=user)
        chat_room_visits = ChatRoomVisit.objects.filter(profile=profile).order_by("-time_visited")[:10][::-1]
        empty = len(list(chat_room_visits)) == 0
        # print(chat_room_visits)
    except (User.DoesNotExist, Profile.DoesNotExist):
        messages.warning(request, f"Profile not found: {profile_name}")
        return redirect("userwall")
    return render(
        request, "userwall/pwall.html", {"profile": profile, "chat_room_visits": chat_room_visits, "empty": empty}
    )


def default(request):
    if request.method == "POST":
        form = WallCreationForm(request.POST)
        if form.is_valid():
            profile_name = form.cleaned_data["username"]
            return redirect("wall1", profile_name)
        messages.warning(request, "Invalid input")

    else:
        form = WallCreationForm()
    return render(request, "userwall/index.html", {"form": form})
