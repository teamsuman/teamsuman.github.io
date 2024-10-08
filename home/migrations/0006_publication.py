# Generated by Django 4.0 on 2024-09-16 09:59

import django.core.validators
from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('training_year', models.PositiveIntegerField(default=2024, validators=[django.core.validators.MinValueValidator(2005), home.models.max_value_current_year])),
                ('authors', models.TextField()),
                ('journal', models.TextField()),
            ],
        ),
    ]
