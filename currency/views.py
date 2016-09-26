
from django.shortcuts import render

from .models import Currency

# Create your views here.
def home(request):
    title = "Welcome!"
    context = {
        # "auth" : auth,
        "prediction" : sum(currencies)
    }


    return render(request, "home.html", context)
