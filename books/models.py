import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title



class Review(models.Model):
    book=models.ForeignKey(
        Book,
        on_delete=models.CASCADE,

    )
    review=models.CharField(max_length=200)
    author=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review