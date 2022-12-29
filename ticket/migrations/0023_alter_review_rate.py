# Generated by Django 4.1.3 on 2022-12-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0022_rename_title_review_review_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 étoile'), (2, '2 étoiles'), (3, '3 étoiles'), (4, '4 étoiles'), (5, '5 étoiles')], default=3, verbose_name='Note'),
        ),
    ]
