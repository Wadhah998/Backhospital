# Generated by Django 3.2.1 on 2021-08-10 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
