# Generated by Django 4.1.3 on 2022-12-12 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0006_remove_photo_caption_alter_critique_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='critique',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
