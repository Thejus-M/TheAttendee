# Generated by Django 4.1 on 2022-09-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teacher", "0003_class"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="class",
            name="student",
        ),
        migrations.AlterField(
            model_name="attendant",
            name="attendants",
            field=models.BooleanField(default=False),
        ),
    ]
