# Generated by Django 4.2.4 on 2023-08-28 11:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0004_review"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resources",
            name="rate",
        ),
    ]
