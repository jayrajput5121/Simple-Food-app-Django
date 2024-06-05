# Generated by Django 5.0.6 on 2024-06-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=500)),
                ('food_description', models.TextField()),
                ('food_image', models.ImageField(upload_to='foodimages')),
            ],
        ),
    ]
