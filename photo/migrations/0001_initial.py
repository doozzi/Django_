# Generated by Django 3.2.16 on 2023-01-19 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
