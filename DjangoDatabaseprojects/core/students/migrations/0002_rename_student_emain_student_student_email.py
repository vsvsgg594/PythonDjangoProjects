# Generated by Django 4.2.4 on 2023-08-25 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student", old_name="student_emain", new_name="student_email",
        ),
    ]
