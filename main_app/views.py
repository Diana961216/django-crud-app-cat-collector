from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# # Create a list of Cat instances
# cats = [
#     Cat("Lolo", "tabby", "Kinda rude.", 3),
#     Cat("Sachi", "tortoiseshell", "Looks like a turtle.", 0),
#     Cat("Fancy", "bombay", "Happy fluff ball.", 4),
#     Cat("Bonk", "selkirk rex", "Meows loudly.", 6),
# ]


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, "home.html")


def about(request):
    return render(
        request, "about.html"
    )  # DTL Django Template Language. this checks for a file named about.html in the templates folder


def cat_index(request):
    cats = Cat.objects.all()  # look familiar?
    return render(request, "cats/index.html", {"cats": cats})


def cat_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, "cats/detail.html", {"cat": cat})


class CatCreate(CreateView):
    model = Cat
    fields = "__all__"  # all fields of the Cat model
    # template_name = "cats/cat_form.html"
    # success_url = "/cats/"  # redirect to the cat index after a successful create


class CatUpdate(UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ["breed", "description", "age"]


class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"
