# Generated by Django 4.2.4 on 2023-08-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vegetables",
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
                ("receipe_name", models.CharField(max_length=100)),
                ("receipe_description", models.TextField()),
                ("receipe_image", models.ImageField(upload_to="receipe")),
            ],
        ),
    ]
