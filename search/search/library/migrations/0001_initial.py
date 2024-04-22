# Generated by Django 5.0.3 on 2024-03-30 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=20, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=13)),
                ('file', models.FileField(upload_to='books/')),
            ],
        ),
    ]
