# Generated by Django 4.1.3 on 2022-12-12 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0011_alter_critique_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='critique',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.ticket'),
        ),
    ]
