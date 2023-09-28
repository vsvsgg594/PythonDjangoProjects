# Generated by Django 4.2.4 on 2023-08-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_remove_students_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_name", models.CharField(max_length=100)),
                ("speed", models.IntegerField()),
            ],
        ),
    ]
