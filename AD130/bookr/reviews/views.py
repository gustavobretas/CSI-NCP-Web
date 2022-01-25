from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})


def home_page(request):
    message = "<html><h1>Welcome to my Website</h1></html>"
    return HttpResponse(message)


def welcome_view(request):
    message = f"<html><h1>Welcome to Bookr!</h1> <p>" \
              f"{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)
