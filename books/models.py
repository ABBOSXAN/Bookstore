import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class ArtBook(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    class Meta:
        indexes=[
            models.Index(fields=['id'], name='id_index'),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])

class TextBook(ArtBook):
    def __init__(self):
        super().__init__()

class Review(models.Model):
    book = models.ForeignKey(
        TextBook,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
