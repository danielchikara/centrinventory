# Generated by Django 4.1.5 on 2023-05-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='creation_date',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]
