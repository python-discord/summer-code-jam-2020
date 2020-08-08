from django.shortcuts import render, redirect
from userwall.models import Wall
from userwall.forms import WallCreationForm

# Create your views here.

def test(request, wall_name):
    print("default", request)
    return render(request, 'userwall/potato.html', {'title': 'test'})

def wall(request, wall_name):

    #print(request)
    #print(wall_name)    

    try:
        wall = Wall.objects.get(name=wall_name)
    except (Wall.DoesNotExist):
        messages.warning(request, f"Profile not found: {wall_name}")
        return redirect("chat")
    return render(request, 'userwall/potato.html')


def default(request):
    
    #print(request)
    if request.method == "POST":
        form = WallCreationForm(request.POST)
        if form.is_valid():
            wall_name = form.cleaned_data["name"]
            print(wall_name)
            wall, _ = Wall.objects.get_or_create(name=wall_name)
            return redirect("wall1", wall_name)
            
    else:
        form = WallCreationForm()
    return render(request, "userwall/index.html", {"form": form})