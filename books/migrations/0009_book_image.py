# Generated by Django 3.2.4 on 2021-06-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
