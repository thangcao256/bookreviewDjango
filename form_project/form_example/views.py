from django.shortcuts import render
from .forms import ExampleForm


# Create your views here.
# def form_example(request):
#     form = ExampleForm()
#     for name in request.POST:
#         print("{}: {}".format(name, request.POST.getlist(name)))
#     # return render(request, "form-example.html", {"method": request.method})
#     return render(request, "form-example.html", {"method": request.method, "form": form})


def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
    else:
        form = ExampleForm()
    if request.method == "POST":
        form = ExampleForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))
    return render(request, "form-example.html", {"method": request.method, "form": form})
