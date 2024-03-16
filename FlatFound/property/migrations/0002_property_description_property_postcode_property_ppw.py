# Generated by Django 5.0.3 on 2024-03-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="postcode",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="ppw",
            field=models.FloatField(default=12),
            preserve_default=False,
        ),
    ]
