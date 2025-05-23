# Generated by Django 4.2 on 2025-04-06 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurantfeature", "0006_remove_product_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gallery",
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
                (
                    "image_1",
                    models.ImageField(default="default.jpg", upload_to="galleryimage/"),
                ),
                (
                    "image_2",
                    models.ImageField(default="default.jpg", upload_to="galleryimage/"),
                ),
            ],
        ),
    ]
