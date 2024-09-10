from django.db import migrations, models
import uuid

def forwards_func(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    for book in Book.objects.all():
        book.new_id = uuid.uuid4()
        book.save()

def backwards_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_cover_alter_book_id'),
    ]

    operations = [
        migrations.RunPython(forwards_func, backwards_func),
    ]


