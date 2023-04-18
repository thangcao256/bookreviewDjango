from django.shortcuts import render
from .forms import ExampleForm, OrderForm


# Create your views here.
# def form_example(request):
#     form = ExampleForm()
#     for name in request.POST:
#         print("{}: {}".format(name, request.POST.getlist(name)))
#     # return render(request, "form-example.html", {"method": request.method})
#     return render(request, "form-example.html", {"method": request.method, "form": form})


# def form_example(request):
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#     else:
#         form = OrderForm()
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#     if form.is_valid():
#         for name, value in form.cleaned_data.items():
#             print("{}: ({}) {}".format(name, type(value), value))
#     return render(request, "form-example.html", {"method": request.method, "form": form})

def form_example(request):
    initial = {"email": "user@solid.edu.vn"}
    if request.method == "POST":
        form = OrderForm(request.POST, initial=initial)
    else:
        form = OrderForm(initial=initial)
    if request.method == "POST":
        form = OrderForm(request.POST)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))
    return render(request, "form-example.html", {"method": request.method, "form": form})
