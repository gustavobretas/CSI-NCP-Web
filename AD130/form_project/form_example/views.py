from django.shortcuts import render


# Create your views here.
from .forms import ExampleForm


def form_example(request):
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "form-example.html", {"method": request.method})


def view_function(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "template.html", {"method": request.method, "form": form})