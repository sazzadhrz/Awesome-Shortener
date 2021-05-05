# Generated by Django 3.2 on 2021-05-04 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shorturl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_url', models.CharField(max_length=10)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
