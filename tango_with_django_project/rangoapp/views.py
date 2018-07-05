from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("""Rango says het there partner
     <a href='/rangoapp/about'>About</a>""")


def about(request):
    return HttpResponse("""Rango says here is the about page
                           <a href='/rangoapp/'> home</a>
                        """)
