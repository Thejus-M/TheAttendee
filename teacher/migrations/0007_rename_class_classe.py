# Generated by Django 4.1 on 2022-09-04 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teacher", "0006_remove_class_student_class_student"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Class",
            new_name="Classe",
        ),
    ]
