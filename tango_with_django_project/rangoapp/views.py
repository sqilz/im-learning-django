from django.shortcuts import render
from django.http import HttpResponse
from rangoapp.models import Category
# Create your views here.


def index(request):
    # Query the database for a list of ALL categories currently stored
    # Order the categories by no. like in descending order
    # Retrieve the top 5 only - or all if less than 5.
    # place the list in our context_dict dictionary
    # that will be passed to the template engine
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    # Render the response and send it back
    return render(request, 'rangoapp/index.html', context=context_dict)


def about(request):
    context_dict = {'me': "Przemek"}
    return render(request, 'rangoapp/about.html', context=context_dict)
