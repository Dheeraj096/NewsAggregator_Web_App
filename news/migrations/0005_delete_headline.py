# Generated by Django 4.2.1 on 2023-07-23 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_headline_description_alter_headline_image_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Headline',
        ),
    ]
