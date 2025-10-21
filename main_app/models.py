from django.db import models
from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.models import User

MEALS = (("B", "Breakfast"), ("L", "Lunch"), ("D", "Dinner"))


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField("Toy")
    # Relate Cat to a User
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "cat-detail", kwargs={"cat_id": self.id}
        )  # used to redirect after creating a new cat


class Feeding(models.Model):
    date = models.DateField("Feeding date", default=timezone.now)
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0],
    )
    # create the cat_id FK
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # get_meal_display() returns the human-readable value of the meal field
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]  # order by date descending


# Add the Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("toy-detail", kwargs={"pk": self.id})
