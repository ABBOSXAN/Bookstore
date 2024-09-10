from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_new_id_book_cover_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='new_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.RemoveField(
            model_name='book',
            name='new_id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='new_id',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True),
        ),
    ]
