from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # for function based views
from django.contrib.auth.mixins import LoginRequiredMixin  # for class based views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Cat, Toy
from .forms import FeedingForm


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect("cat-index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)
    # Same as:
    # return render(
    #     request,
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


@login_required
def cat_index(request):
    # Only show the signed-in user's cats
    cats = Cat.objects.filter(user=request.user).order_by("name")
    return render(request, "cats/index.html", {"cats": cats})


@login_required
def cat_detail(request, cat_id):
    # Only allow access to the owner's cat
    cat = Cat.objects.get(id=cat_id)
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list("id"))
    feeding_form = FeedingForm()
    return render(
        request,
        "cats/detail.html",
        {
            "cat": cat,
            "feeding_form": feeding_form,
            "toys": toys_cat_doesnt_have,
        },
    )


@login_required
def add_feeding(request, cat_id):
    # Ensure the feeding is added only to the current user's cat
    cat = get_object_or_404(Cat, id=cat_id, user=request.user)
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat = cat
        new_feeding.save()
    return redirect("cat-detail", cat_id=cat_id)


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ["name", "breed", "description", "age"]

    def form_valid(self, form):
        # Assign ownership to the logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = ["breed", "description", "age"]

    def get_queryset(self):
        # Users can only update their own cats
        return Cat.objects.filter(user=self.request.user)


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = "/cats/"

    def get_queryset(self):
        # Users can only delete their own cats
        return Cat.objects.filter(user=self.request.user)


@login_required
def associate_toy(request, cat_id, toy_id):
    # Note that you can pass a toy's id instead of the whole object
    Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect("cat-detail", cat_id=cat_id)


@login_required
def remove_toy(request, cat_id, toy_id):
    Cat.objects.get(id=cat_id).toys.remove(toy_id)
    return redirect("cat-detail", cat_id=cat_id)


class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = "__all__"


class ToyList(LoginRequiredMixin, ListView):
    model = Toy


class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy


class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ["name", "color"]


class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = "/toys/"


class Home(LoginView):
    template_name = "home.html"
