from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<em>My second project</em>")

def help(request):
    help_dict = {"help_me": "This is a help page"}
    return render(request, "second_app/help.html", help_dict)