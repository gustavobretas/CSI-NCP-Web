from django.shortcuts import render


# Create your views here.
from form_example.forms import ExampleForm


def form_example(request):
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "form-example.html", {"method": request.method})


def view_function(request):
    form = ExampleForm()
    return render(request, "template.html", {"form": form})