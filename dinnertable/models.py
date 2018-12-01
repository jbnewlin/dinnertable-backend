from django.contrib.postgres.fields import ArrayField
from django.db import models


class Recipe(models.Model):
    """
    Model for recipes.

    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=False, verbose_name="Name of the recipe")
    description = models.CharField(max_length=1000, blank=True, verbose_name="A description about the recipe")
    ingredients = ArrayField(ArrayField(models.CharField(max_length=100, blank=False)))
    steps = ArrayField(ArrayField(models.CharField(max_length=300, blank=False)))

