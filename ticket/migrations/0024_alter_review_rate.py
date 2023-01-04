# Generated by Django 4.1.3 on 2023-01-04 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0023_alter_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='Note'),
        ),
    ]
