# Generated by Django 4.1.3 on 2022-12-08 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_critique'),
    ]

    operations = [
        migrations.AddField(
            model_name='critique',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket'),
        ),
        migrations.AlterField(
            model_name='critique',
            name='rate',
            field=models.CharField(choices=[('1', '1 étoile'), ('2', '2 étoiles'), ('3', '3 étoiles'), ('4', '4 étoiles'), ('5', '5 étoiles')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='content',
            field=models.TextField(max_length=5000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Titre du livre'),
        ),
    ]