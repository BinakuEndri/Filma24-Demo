from django.shortcuts import render
from filma.models import *


def home_content(request):
    return render(request,"land_template/home.html")

