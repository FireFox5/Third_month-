from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='blog_images/')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('likes', models.IntegerField()),
                ('reposts', models.IntegerField()),
            ],
        ),
    ]