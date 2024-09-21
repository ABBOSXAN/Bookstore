from django.contrib import admin
from .models import ArtBook, TextBook, Review


# Register your models here.

class ReviewInline(admin.TabularInline):
    model = Review


class ArtBookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline, ]
    list_display = ('title', 'author', 'price')


class TextBookAdmin(admin.ModelAdmin):
    list_display = ('title', "muallif", 'narx')


admin.site.register(ArtBook, TextBook, ArtBookAdmin, TextBookAdmin)
