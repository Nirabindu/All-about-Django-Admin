# Generated by Django 4.1.2 on 2022-10-07 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("-date_added",),
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.AlterModelOptions(
            name="subcategory",
            options={
                "verbose_name": "Sub Category",
                "verbose_name_plural": "SubCategories",
            },
        ),
    ]
