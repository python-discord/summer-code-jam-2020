from django.shortcuts import get_object_or_404, render
from .models import Account

def earl_list_view(request):
    queryset = Account.objects.all()
    context = {
        "earl_list": queryset,
        "users": queryset.filter(is_user=True),
        "ficthist": queryset.filter(is_user=False),
        "active_page": "browse",
    }
    return render(request, "earls/earllist.html", context)
