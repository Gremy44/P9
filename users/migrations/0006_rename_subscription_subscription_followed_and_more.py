# Generated by Django 4.1.3 on 2022-12-16 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='subscription',
            new_name='followed',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='subscriber',
            new_name='follower',
        ),
    ]
