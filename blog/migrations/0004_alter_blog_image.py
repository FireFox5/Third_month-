# Generated by Django 3.2.8 on 2021-10-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211025_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog_images/'),
        ),
    ]
