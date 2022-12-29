# Generated by Django 4.1.3 on 2022-12-13 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0018_alter_critique_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critique',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='critique',
            name='ticket',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket'),
            preserve_default=False,
        ),
    ]