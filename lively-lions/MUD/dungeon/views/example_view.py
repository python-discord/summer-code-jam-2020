from django.http import HttpResponse


# CRUD
def rest(request):
    # Read
    if request.method == "GET":
        return HttpResponse("Working GET")
    # Create
    if request.method == "POST":
        if request.POST["num"]:
            return HttpResponse("Working POST " + request.POST["num"])
        else:
            return HttpResponse("Working POST")
