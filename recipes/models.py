from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    serving_time = models.IntegerField()
    serbing_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    create_at = models.DateTimeField(
        auto_now_add=True
    )  # cria a data no momento da criação sem alteração depois
    update_at = models.DateTimeField(
        auto_now=True
    )  # atualiza o campo automaticamente depois de salvar
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to="recipes/cover/%Y/%m/%d/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
